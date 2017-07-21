#!/usr/bin/python
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

'''

def hamming_dist(s,t):
    s = bin(s)[2:]
    t = bin(t)[2:]
    if len(s) > len(t):
        t = t.zfill(len(s))
    else:
        s = s.zfill(len(t))
    count = 0
    for i in range(len(s)):
        if t[i] != s[i]:
            count += 1
    return count

if __name__ == "__main__":
    s = 12
    t = 56
    print hamming_dist(s,t)

