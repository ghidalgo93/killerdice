# Gerardo Hidalgo-Cuellar
# KillerDice, a dice rolling application that will roll dice for you
# 8/5/2020 https://github.com/ghidalgo93

# Import Libraries
import random
import re
from helperfunctions import roll

# Define variables
rawdice = []
moddice = []
totdice = 0

# Dice/Roll expression entered in the form *number of dice*d*kind of dice* +- *modifier*
# ** example 3d20 + 8 **
roll = roll()

# Split on the "d" and "+/-", will include those delimeters in the list, ie. [2, d, 6, +, 1]
split = re.split('([d+-])', roll)

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
