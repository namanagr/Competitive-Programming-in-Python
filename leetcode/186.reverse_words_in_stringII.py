#!/usr/bin/python
#Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
#The input string does not contain leading or trailing spaces and the words are always separated by a single space.
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".
#Could you do it in-place without allocating extra space?

def rev(s, i, j):
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    return "".join(s)

def reverseWords(s):
    i = 0
    s = list(s)
    for j in range(len(s)):
        if s[j] == " ":
            rev(s,i,j-1)
            i = j+1
    rev(s,i,len(s)-1)
    rev(s,0,len(s)-1)
    return "".join(s)

if __name__ == "__main__":
    s = "the sky is blue"
    print reverseWords(s)
