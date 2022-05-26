file_in = open("filein.txt", "r")
# This line opens the input text file in read mode specifically ("r"), and stores it as a variable
print(file_in)
# As you can see by the print statement, it just creates some code for python to understand

file_out = open("fileout.txt", "w")
# Similarly, we can open the output file in write mode ("w")

print(f"\nThe output of read() is: \n{file_in.read()}\n")
# The read() function reads the whole file
file_in.seek(0)

print(f"The output of readline() is: \n{file_in.readline()}")
# The readline() function reads one line
file_in.seek(0)

print(f"The output of readlines() is: \n{file_in.readlines()}\n")
# The readline() function reads one line
file_in.seek(0)

# Note: if a bit has already been read, it moves where python is reading the line from. This can be changed with seek()
# Therefore, by default readline() reads the first line and if it is called again will then read the second line etc


# Finally, to write, you just use the write function and input a variable
input = "I wrote this to a file!"
file_out.write(input)

# You can use this as a basic template for the AIO
# Hope that makes sense :D
