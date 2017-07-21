#!/usr/bin/python

'''
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

def single_num(arr): # using hashmap # better performance
    map = {}
    for num in arr:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    for key in map:
        if map[key] != 2:
            return key

def single_num_set(arr): # using set
    nums = set()
    for num in arr:
        if num not in nums:
            nums.add(num)
        else:
            nums.remove(num)
    for val in nums:
        return val


if __name__ == "__main__":
    arr = [1,1,2,3,3]
    print single_num_set(arr)

