import re

foo = "2d6"

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


print(bar)
print(dnum)
print(dtype)
print(dmod)