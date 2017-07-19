#!/usr/bin/python
'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

def iso_check(s,words):
    map_s = {}
    map_w = {}
    words = words.split(" ")
    if len(words) != len(s):
        return False
    for i in range(len(s)):
        if s[i] not in map_s and words[i] not in map_w:
            map_s[s[i]] = words[i]
            map_w[words[i]] = s[i]
        elif s[i] not in map_s or words[i] not in map_w:
            return False
        elif map_s[s[i]] != words[i] or map_w[words[i]] != s[i]:
            return False
    return True

if __name__ == "__main__":
    s = "abba"
    words = "dog cat cat dog"
    print naman_iso_check(s,words)