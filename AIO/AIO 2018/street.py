import math

streetin = open("streetin.txt","r")
streetout = open("streetout.txt","w")
input = streetin.read();
output = '';
input = input.split(' ');
numhouse = int(input[0]) - int(input[1]);
groups = int(input[1]) + 1;
output = divmod(numhouse, groups)[0];

if divmod(numhouse, groups)[1] != 0:
    output += 1;

print(input)
print(output);

streetout.write(str(output));
streetin.close();
streetout.close();