import random
import re

#dice expression entered in the form *number of dice*d*kind of dice* +- *modifier*
#example 3d20 + 8
dice = input("What dice dawg? ")

#some kind of input catch to make sure the user didn't fuck up

# pattern to split on: on the "d" and "+/-"
split = re.split('[d+-]', dice)

#getting each of the input diameters
dnum = int(split[0])
dkind = int(split[1])
mod =  int(split[2])

#roll each die and add it to dice total
dtotal = 0
for i in range(dnum):
    n = random.randint(1,dkind)
    print(n)
    dtotal = dtotal + n
    #need to add modifier 

print(dtotal)

