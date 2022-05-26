import sys

def remval(the_list, val):
    return [value for value in the_list if value != val]

def close(input):
    cavalryout.write(input)
    cavalryin.close()
    cavalryout.close()
    sys.exit()

cavalryin = open("cavalryin.txt","r")
cavalryout = open("cavalryout.txt","w")
input = cavalryin.read()
input = input.split('\n')
numsum = 0;

numKnights = int(input.pop(0))

while True:
    try:
        if input.count(input[0]) % int(input[0]) == 0:
            numsum += input.count(input[0])
        else:
            close('NO')
        input = remval(input,input[0])
    except:
        break

if numsum == numKnights:
    close('YES')
else:
    close('NO')