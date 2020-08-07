import re
import random

# A die/dice class, holds and rolls info about the die
# input: [int] sides, [int] modifier
class Die:
    def __init__(self, sides, modifier):
        self.sides = sides                  
        self.modifier = modifier
        roll = random.randint(0, sides)
        self.rawRoll = roll
        self.modRoll = roll + modifier

foo = "4d20 - 5"

if re.fullmatch('\d+d\d+[+-]{0,1}\d*', foo.replace(" ", "")):
    print("success")
else:
    print("fail")

bar = re.split('([d+-])', foo.replace(" ", ""))


dnum = int(bar[0])
dtype = int(bar[2])


if len(bar) > 3:
    dmod = int(bar[3] + bar[4])
else:
    dmod = 0

dicelist = []

for i in range(dnum):
    dicelist.append(Die(dtype, dmod))

for d in dicelist:
    print(d.modRoll)