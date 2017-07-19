#!/usr/bin/python
#Convert Roman number to Integer

def roman_to_integer(roman):
    map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    '''
    map["I"] = 1
    map["V"] = 5
    map["X"] = 10
    map["L"] = 50
    map["C"] = 100
    map["D"] = 500
    map["M"] = 1000
    '''
    num = []
    sum = 0
    for literal in roman:
        num.append(map[literal])
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            sum -= num[i]
        else:
            sum += num[i]
    return sum + num[len(num)-1]

def romanToInt(self, s):
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    for i in range(len(s) - 1):
        if map[s[i]] < map[s[i + 1]]:
            sum -= map[s[i]]
        else:
            sum += map[s[i]]
    sum += map[s[len(s) - 1]]
    return sum

if __name__ == "__main__":
    roman = "VII"
    print roman_to_integer(roman.upper())
