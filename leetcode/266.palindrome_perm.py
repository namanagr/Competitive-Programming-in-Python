#!/usr/bin/python
#Find if the characters of a given word can be shuffled to form a valid palindrome

def isPalindrome(word):
    map = {}
    for literal in word:
        if literal not in map:
            map[literal] = 1
        else:
            map[literal] += 1
    odd = 0
    for entry in map:
        if map[entry]%2 != 0:
            odd += 1
    if odd > 1:
        return False
    else:
        return True

if __name__ == "__main__":
    word = "carerac"
    print isPalindrome(word)