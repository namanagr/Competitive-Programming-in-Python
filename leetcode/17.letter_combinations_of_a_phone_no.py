#!/usr/bin/python
#Given two keys of a mobile keypad.
#Return all possible combinations that can be generated from that keypad.

def combinations(digits):
    if not digits:
        return []
    if '0' in digits or '1' in digits:
        return []
    for digit in digits:
        if not digit.isdigit():
            return [ ]
    keypad = {
        #'0': "",
        #'1': "",
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    arr = []
    str = ""
    for digit in digits:


if __name__ == "__main__":
    digits = "23"
    print combinations(digits)