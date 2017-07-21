#!/usr/bin/python
# This program searches an element in a rotated sorted array

def binarysearch(bs_arr, left, right, val):
    mid = (right-left)/2
    notFound = True

    while left <= right and notFound:
        if bs_arr[mid] == val:
            notFound = False
        elif bs_arr[mid] < val:
            left = mid+1
        else:
            right = mid-1
        mid = (left + right)/2
    if notFound == False:
        return mid
    else:
        return -1

def search(s_arr, left, right, val):
    mid = (left + right)/2
    if s_arr[mid] == val:
        res = mid
    elif s_arr[0] < s_arr[1] and val >= s_arr[0] and val <= s_arr[mid]:
        res = binarysearch(s_arr, 0, mid-1, val)
    else:
        res = search(s_arr, mid+1, len(s_arr)-1, val)
    return res

if __name__ == "__main__":
    #arr = [4 5 6 7 0 1 2]
    arr = [10,11,12,13,14,1,2,3,4,5,6,7,8,9]
    val = 7
    print search(arr, 0, len(arr)-1, val)