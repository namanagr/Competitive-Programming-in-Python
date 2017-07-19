#!/usr/bin/python

'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
'''

def rewardCheck(s):
    a_cnt = 0
    l_cnt = 0
    for c in s:
        if c == "A":
            a_cnt += 1
            l_cnt = 0
        elif c == "L":
            l_cnt += 1
        else:
            l_cnt = 0
        if a_cnt > 1 or l_cnt > 2:
            return False
    return True

if __name__ == "__main__":
    s = "PPALLP"
    print rewardCheck(s)