#!/usr/bin/python
#Check if the strings are isomorphic or not

def iso_check(s,p):
    map_s = {}
    map_p = {}
    if len(s) != len(p):
        return False
    for i in range(len(s)):
        if s[i] not in map_s and p[i] not in map_p:
            map_s[s[i]] = p[i]
            map_p[p[i]] = s[i]
        elif s[i] not in map_s or p[i] not in map_p:
            return False
        elif map_s[s[i]] != p[i] or map_p[p[i]] != s[i]:
            return False
    return True

if __name__ == "__main__":
    s = "ab"
    p = "aa"
    print iso_check(s,p)