magicin = open("magicin.txt","r")
magicout = open("magicout.txt","w")
input = magicin.read()
input = input.split(' ')
sum = int(input[0]) + int(input[1]) + int(input[2])

a1 = int(input[0])
b1 = int(input[1])
a2 = int(input[2])

c1 = sum - (a1 + b1)
a3 = sum - (a1 + a2)
b2 = sum - (c1 + a3)
c2 = sum - (a2 + b2)
b3 = sum - (b1 + b2)
c3 = sum - (c1 + c2)

magicout.write(str(a1) + ' ' + str(b1) + ' ' + str(c1) + '\n')
magicout.write(str(a2) + ' ' + str(b2) + ' ' + str(c2) + '\n')
magicout.write(str(a3) + ' ' + str(b3) + ' ' + str(c3) + '\n')
magicin.close()
magicout.close()