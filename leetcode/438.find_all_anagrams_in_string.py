#!/usr/bin/python
# This program finds all anagrams in a string

def all_anagrams(s,p):
    len_p = len(p)
    indices = []
    for i in range(len(s)-len_p+1):
        tracker = "0" * len_p
        for j in range(i,i+len_p):
            if s[i] in p:
                tracker[s.index(s[i])] = 1
        print "".join(tracker), "1"*len_p
        if tracker == "1"*len_p:
            indices.append(i)
    return indices

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print all_anagrams(s,p)

