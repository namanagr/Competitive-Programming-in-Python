#!/usr/bin/python

def ispalindrome(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    arr = "abbddbbadd"
    print ispalindrome(arr)
    