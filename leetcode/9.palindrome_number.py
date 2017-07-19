#!/bin/bash
# This program checks if a number is a palindrome or not

def isPalindrome(x):
    if x < 0 or (x > 0 and x%10 == 0):
        return False
    rev = 0
    while rev < x:
        rev = rev*10 + x%10
        x = x%10
    return rev == x or rev/10 ==x

if __name__ == "__main__":
    print isPalindrome(12321)
    print isPalindrome(-123213)