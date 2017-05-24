#!/usr/bin/python
#Checks whether s is a valid anagram of t

def isAnagram(s, t):
    map = {}
    for literal in t:
        if literal not in map:
            map[literal] = 1
        else:
            map[literal] += 1
    for literal in s:
        if literal not in map:
            return False
        else:
            map[literal] -= 1
    for element in map:
        if map[element] != 0:
            return False
    return True

s = "anagram"
t = "garmaan"
print isAnagram(s,t)