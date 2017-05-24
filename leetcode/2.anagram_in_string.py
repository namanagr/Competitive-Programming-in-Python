#!/usr/bin/python
# This program finds the starting index of the anagrams of string p in s

def anagram(s,p):
    pmap = {}
    smap = {}
    if p is None or s is None or len(p) > len(s):
        return []
    for literal in p:
        if literal not in map:
            map[literal] = 1
        else:
            map[literal] += 1
    for i in range(len(s)):
        reset = 0


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print anagram(s,p)
