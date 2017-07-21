#!/usr/bin/python
# This program reverses a string

def reverse(s):
    s = list(s)
    i = 0
    j = len(s)-1
    while i<j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    return "".join(s)


if __name__ == "__main__":
    s = "hello"
    print reverse(s)