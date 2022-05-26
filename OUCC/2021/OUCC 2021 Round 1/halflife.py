from decimal import *

userIn = input().split(" ")
mass = int(userIn[0])
hlife = int(userIn[1])
n = int(userIn[2])

print(hlife * n)
print(Decimal(str(mass / (2 ** n))).quantize(Decimal('1.0000')))
