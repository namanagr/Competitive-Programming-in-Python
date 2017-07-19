#!/usr/bin/python
# This program reverses only the vowels of a string

def reverseVowels(s):
    s = list(s)
    vowels = "aeiouAEIOU"
    i = 0
    j = len(s)-1
    while i < j:
        while i<j and s[i] not in vowels:
            i += 1
        while i<j and s[j] not in vowels:
            j -= 1
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    return "".join(s)

if __name__ == "__main__":
    s = "leetcode"
    print reverseVowels(s)