#!/usr/bin/python
# This program converts Integer to Roman

def int_to_roman(num):
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    output = ""                                     e
    for i in range(len(vals)):
        while num > vals[i]:
            num -= vals[i]
            output += strings[i]
    return output

if __name__ == "__main__":
    num = 1234
    print int_to_roman(num)