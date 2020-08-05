# Gerardo Hidalgo-Cuellar
# Helper functions for KillerDice
# 8/5/2020 https://github.com/ghidalgo93

# Import libraries
import re

# A function which asks the user for their roll, gives them dirctions and asks them again if incorrect format
# input: NONE
# output: [string] the correctly formatted roll
'''
def roll():
    rollInput = input("Roll: ").replace(" ", "")                        #get roll input and strip white space
    if not re.fullmatch('\d+d\d+[+-]{0,1}\d*', rollInput):                  #make sure correct format
        print("Format:(# of dice) d (type of dice) +/- (modifier) ")    #give format
        roll()                                                          #recursively call itself
    else:
        print(rollInput)
        return(rollInput)                                               #given correct format return the roll string
'''

def roll():
    rollInput = input("Roll: ").replace(" ", "")                            #get roll input and strip white space
    while not re.fullmatch('\d+d\d+[+-]{0,1}\d*', rollInput):               #make sure format is correct
        print("Format:(# of dice) d (type of dice) +/- (modifier) ")        #print format
        rollInput = input("Roll: ").replace(" ", "")                        #get roll input and strip wite space
    return(rollInput)                                                       #return roll input as string