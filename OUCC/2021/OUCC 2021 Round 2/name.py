name = list(input())
shift = []
y = 4

while y > 0:
    for x in range(y):
        shift.append(name.pop(0))

    for x in shift:
        name.insert(0, x)

    shift = []
    y = y - 1

print("".join(name))
