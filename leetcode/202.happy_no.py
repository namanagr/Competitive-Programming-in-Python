#!/usr/bin/python

#Write an algorithm to determine if a number is "happy".
#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#Example 19 is a happy number

def sumdigits(n):
    sum = 0
    while n != 0:
        remainder = n%10
        n = n/10
        sum += remainder*remainder
    return sum

if __name__ == "__main__":
    n = 19
    while True:
        n = sumdigits(n)
        if n <= 6:
            break
    if n == 1:
        print True
