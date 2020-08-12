# Gerardo Hidalgo-Cuellar
# KillerDice, a dice rolling application that will roll dice for you
# 8/5/2020 https://github.com/ghidalgo93

# Import Libraries
import random
import re


def main():
    # Define variables
    userInput = ""
    dice = []
    rawDice = []
    modDice = []
    totalDice = 0

    # Continue to prompt user for dice until they ask to roll
    while userInput.lower() != "roll":
        userInput = input("Add dice or roll: ")         #get the users input
        check = checkInput(userInput)
        if check == 0:                                  # if the user inputs "roll"
            print("rolling...")
        elif check == 1:                                # if the user inputs a valid roll, add it to dice list, then ask again
            for d in createDice(userInput):
                dice.append(d)
        else:                                           # if the users input is invalid, let them know and ask again
            print("type 'roll' to roll dice or add dice with format:(# of dice) d (type of dice) +/- (modifier)")

    # Using the dice list, add those rolls to lists that can be easily printed
    for d in dice:
        rawDice.append(d.rawRoll)
        modDice.append(d.modRoll)
        totalDice = totalDice + d.modRoll
    
    print("Raw Rolls: ", rawDice)
    print("Modified Rolls: ", modDice)
    print("Total Roll: ", totalDice)


##
# Helper functions, eventually put into another file
##

def checkInput(userInput):
    '''
    Returns a format check.
    
        Parameters:
                userInput (str): the user's input
        Returns:
                format type (int): the kind of check, roll (0), correct format (1), incorrect format (2)
    '''
    rollInput = userInput.replace(" ", "")                      #get input and strip white space
    if userInput.lower() == "roll":
        return(0)                                               #roll
    if re.fullmatch('\d+d\d+[+-]{0,1}\d*', rollInput):          
        return(1)                                               #correct format
    else:
        return(2)                                               #incorrect format

def createDice(userInput):
    '''
    Returns a list of dice instances.

        Parameters:
                userInput (str): the correctly formatted user's input
        Returns:
                dice (list): a list of dice
    '''
    dice = []
    # Strip white space and split on the "d" and "+/-", will include those delimeters in the list, ie. [2, d, 6, +, 1]
    userInput = userInput.replace(" ", "")
    split = re.split('([d+-])', userInput)
    
    # Get dice parameters from the string split
    numberOfDice = int(split[0])                        #dice number
    diceSides = int(split[2])                           #kinf of dice
    if len(split) > 3:                                  #if there is a modifier, add it
        diceModifier = int(split[3] + split[4])
    else:                                                #if no modifier provided, modifier will be 0
        diceModifier = 0

    for d in range(numberOfDice):                       #create and append dice designated by diceNumber to dice list
        dice.append(Die(diceSides,diceModifier))            
    return(dice)                                        #return dice list


# A die/dice class, holds and rolls info about the die
# input: [int] sides, [int] modifier
class Die:
    """
    A class to represent a die.
    ...
    
    Attributes
    ----------
    sides : int
        the number of sides the dice has
    modifier : int
        the modifier to be added to roll
    rawRoll : int 
        the randomized roll based off the number of sides
    modRoll : int
        the modified roll (rawRoll + modifier)
    """
    def __init__(self, sides, modifier):
    """
        Constructs all the necessary attributes for the die object.

        Parameters
        ----------
        sides : int
            the number of sides the dice has
        modifier : int
            the modifier to be added to roll
        rawRoll : int 
            the randomized roll based off the number of sides
        modRoll : int
            the modified roll (rawRoll + modifier)
    """
        self.sides = sides                  
        self.modifier = modifier
        roll = random.randint(0, sides)
        self.rawRoll = roll
        self.modRoll = roll + modifier

main()