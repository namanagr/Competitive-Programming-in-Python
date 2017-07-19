#!/usr/bin/python
# This program finds the longest substring without repeating characters.

'''
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def longest_substr(s): # Returns the length of the longest string.
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    map = {}
    start = 0
    max_len = 0
    for i in range(len(s)):
        if s[i] in map:
            start = max(start, map[s[i]] + 1)
        map[s[i]] = i
        max_len = max(max_len, i - start + 1)
    if start == 0:
        return len(s)
    else:
        return max_len

if __name__ == "__main__":
    s = "abcabcbb"
    s1 = "au"
    print longest_substr(s)
    print longest_substr(s1)
