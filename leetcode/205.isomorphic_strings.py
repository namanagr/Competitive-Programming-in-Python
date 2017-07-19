#!/usr/bin/python
#Check if the strings are isomorphic or not

def isIsomorphic(s,p):
    if len(s) != len(p):
        return False
    map_s = {}
    map_p = {}
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
    s = "dd"
    p = "aa"
    print isIsomorphic_using_arrays(s,p)