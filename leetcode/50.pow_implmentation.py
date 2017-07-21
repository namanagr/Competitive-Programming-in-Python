#!/usr/bin/python
# This program implements pow(s,n) function

def pow(x, n): # recursive solution
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == -1:
        if n%2 == 0:
            return 1
        else:
            return -1
    if n == 0:
        return 1
    if n < Integer
    if n < 0:
        x = 1/x
        n = -n
    if n%2 == 0:
        return pow(x*x, n/2)
    else:
        return x*pow(x*x, n/2)


if __name__ == "__main__":
    print pow(2,3)
    print pow(2,-2147483648)