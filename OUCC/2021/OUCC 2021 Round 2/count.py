userIn = int(input())
doNot = 0
if userIn == 0:
    print("0")
    doNot = 1

arr = []
while userIn > 0:
    arr.append(str(userIn))
    userIn = userIn - 1

if doNot == 0:
    print(" ".join(arr))
