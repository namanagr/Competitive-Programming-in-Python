#!/usr/bin/python
# Given two strings 's' and 't'.
# String 't' has shuffled letters of 's' and then one letter was added to it.
# We need to find that letter.

def findTheDifference(s,t):
    map = {}
    for x in s:
        if x not in map:
            map[x] = 1
        else:
            map[x] += 1
    for x in t:
        if x not in map or map[x] == 0:
            return x
        map[x] -= 1

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print findTheDifference(s,t)