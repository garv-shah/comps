userIn = input().split(" ")
newArr = []

for x in range(len(userIn)):
    newArr.append(((x*10)-int(userIn[x])))

print(max(newArr))
