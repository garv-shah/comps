#!/usr/bin/env python
import sys

sys.setrecursionlimit(1000000000)

#
# Solution Template for Melody
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of notes.
N = None

# K is the number of types of notes (labelled from 1 to K).
K = None

answer = 0

# Open the input and output files.
input_file = open("melodyin.txt", "r")
output_file = open("melodyout.txt", "w")

# Read the value of N and K.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())
# S contains the sequence of notes forming the song.
S = [None for x in range(N)]

# Read each note in the song.
for i in range(0, N):
    S[i] = int(input_file.readline().strip())


# TODO: This is where you should compute your solution. Store the smallest
# possible number of notes Melody can change so that her song is nice into the
# variable answer.

first = [0 for x in range(K + 1)]
second = [0 for x in range(K + 1)]
third = [0 for x in range(K + 1)]

# S = [1, 2, 5, 1, 4, 5, 1, 4, 4]
# This is the original melody. We have to find the smallest amount of changes so it sounds "nice"

arrfor1 = S[::3]
# Gets every 3n element
# [1, 1, 1]

# bucket sort
for x in range(len(arrfor1)):
    first[arrfor1[x]] += 1

arrfor2 = S[1::3]
# Gets every 3n + 1 element
# [2, 4, 4]

# bucket sort
for x in range(len(arrfor2)):
    second[arrfor2[x]] += 1

arrfor3 = S[2::3]
# Gets every 3n + 2 element
# [5, 5, 4]

# bucket sort
for x in range(len(arrfor3)):
    third[arrfor3[x]] += 1

arr = [first.index(max(first)), second.index(max(second)), third.index(max(third))]
# arr = [1, 4, 5]
arr = arr * int(N / 3)
# arr = [1, 4, 5, 1, 4, 5, 1, 4, 5]
# this array is closest "nice" melody
# the loop underneath just compares the two arrays to see how many changes need to be made

for x in range(len(arr)):
    if arr[x] != S[x]:
        answer += 1

print(answer)
# 2

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
