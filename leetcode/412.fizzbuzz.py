#!/usr/bin/python
# print fuzz if multiple of 3
# print buzz if multiple of 5

def fizzbuzz(n):
    for i in range(1,n+1):
        s = ""
        if i%3 == 0:
            s += "Fizz"
        if i%5 == 0:
            s += "Buzz"
        if s == "":
            s = str(i)
        print s

if __name__ == "__main__":
    n = 15
    fizzbuzz(n)

