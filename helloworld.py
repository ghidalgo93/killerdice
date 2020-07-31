import random

dsize = int(input("What kind of dice would you like to roll? "))
dnum = int(input("How many of those dice would you like to roll? "))
modQuestion = input("Would you like to add a modifier (y/n)? ")
if modQuestion == 'y':
    mod = int(input("What would you like to add/subtract? "))

dicelist = []
modlist = []

for i in range(0,dnum):
    n = random.randint(1,dsize)
    if modQuestion == 'y':
        modlist.append(n+mod)
    dicelist.append(n)

print(dicelist)
print(modlist)