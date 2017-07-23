#!/usr/bin/python

def convertToTitle(n):
    res = ""
    while n != 0:
        ch = chr((n-1)%26 + 65)
        res = ch + res
        n = (n-1)/26
    return res

if __name__ == "__main__":
    num = 1000
    print convertToTitle(num)