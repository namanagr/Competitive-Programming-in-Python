#!/usr/bin/python
# This program detects and prints the characters which occurs more than once in the string using hashing.

str = "namanisagreatperson."

count = [0]*256
for char in str:
    if count[ord(char)] == 1:
        print char
    count[ord(char)] += 1



