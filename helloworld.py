import random

dsize = int(input("What die would you like to roll?"))
dnum = int(input("How many of those dice would you like to roll?"))

dicelist = []

for i in range(0,dnum):
    n = random.randint(1,dsize)
    dicelist.append(n)

print(dicelist)