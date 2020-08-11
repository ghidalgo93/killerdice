# Gerardo Hidalgo-Cuellar
# KillerDice, a dice rolling application that will roll dice for you
# 8/5/2020 https://github.com/ghidalgo93

# Import Libraries
import random
import re


def main():
    # Define variables
    rawdice = []
    moddice = []
    totdice = 0

    # Dice/Roll expression entered in the form *number of dice*d*kind of dice* +- *modifier*
    # ** example 3d20 + 8 **
    userRoll = roll()

    # Split on the "d" and "+/-", will include those delimeters in the list, ie. [2, d, 6, +, 1]
    split = re.split('([d+-])', userRoll)

    # Get dice parameters from the string split
    dnum = int(split[0])                        #dice number
    dkind = int(split[2])                       #kinf of dice
    if len(split) > 3:                          #if there is a modifier, add it
        dmod = int(split[3] + split[4])
    else:                                       #if no modifier provided, modifier will be 0
        dmod = 0

    # Roll each die, add raw roll to rawdice list, add modifier and add to moddice list, and modified roll to dice total
    for i in range(dnum):
        n = random.randint(1,dkind)
        rawdice.append(n)
        #crit check
        m = n + dmod
        moddice.append(m)
        totdice = totdice + m 

    # Print the raw dice list, modified dice list (if different), and total roll
    print("Raw roll(s): ", rawdice)
    if rawdice != moddice:
        print("Modified roll(s): ",  moddice)
    print("Total sum: ", totdice)




##
# Helper functions, eventually put into another file
##

# A function which asks the user for their roll, gives them dirctions and asks them again if incorrect format
# input: NONE
# output: [string] the correctly formatted roll
def roll():
    rollInput = input("Roll: ").replace(" ", "")                            #get roll input and strip white space
    while not re.fullmatch('\d+d\d+[+-]{0,1}\d*', rollInput):               #make sure format is correct
        print("Format:(# of dice) d (type of dice) +/- (modifier) ")        #print format
        rollInput = input("Roll: ").replace(" ", "")                        #get roll input and strip wite space
    return(rollInput)         

# A die/dice class, holds and rolls info about the die
# input: [int] sides, [int] modifier
class Die:
    def __init__(self, sides, modifier):
        self.sides = sides                  
        self.modifier = modifier
        roll = random.randint(0, sides)
        self.rawRoll = roll
        self.modRoll = roll + modifier

main()


