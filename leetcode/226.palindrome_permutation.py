#!/usr/bin/python
# Checks whether the given string can be a valid palindrome or not

def isvalidpalindrome(s):
    map = {}
    for literal in s:
        if literal not in map:
            map[literal] = 1
        else:
            map[literal] *= -1
    odd = 0
    for item in map:
        if map[item] == 1:
            odd += 1
    if odd > 1:
        return False
    else:
        return True

s = "nmana"
print isvalidpalindrome(s)