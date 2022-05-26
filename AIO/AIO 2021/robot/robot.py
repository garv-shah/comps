#!/usr/bin/env python
import sys

sys.setrecursionlimit(1000000000)

input_file = open("robotin.txt", "r")
output_file = open("robotout.txt", "w")

# Read the value of K and the sequence of instructions from the input file.
K = int(input_file.readline().strip())
arr = list(input_file.readline().strip())

# TODO: This is where you should compute your solution. Store the fewest number
# of instructions you need to add to the end of the sequence into the variable
# answer.

K -= (min(arr.count("W"), arr.count("E")) * 2) + (min(arr.count("S"), arr.count("N")) * 2)

# Write the answer to the output file.
output_file.write(str(K))

# Finally, close the input/output files.
input_file.close()
output_file.close()
