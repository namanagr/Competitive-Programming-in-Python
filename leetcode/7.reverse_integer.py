#!/usr/bin/python
# This program reverses an integer.


def rev(num):
    neg = False
    if num == 0:
        return num
    if num < 0:
        neg = True
        num = -num
    if num >= pow(2,31)-1: #overflow case. Not sure about its correctness. Stupid case.
        return 0
    rev = 0
    while num != 0:
        rev = rev*10 + num%10
        num /= 10
    if neg:
        return -rev
    else:
        return rev


if __name__ == "__main__":
    num = 1534236469
    print rev(num)