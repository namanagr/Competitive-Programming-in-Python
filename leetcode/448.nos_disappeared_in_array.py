#!/usr/bin/python
'''
Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

'''

def findDisappearedNumbers(nums):
    collection = set()
    missing = []
    for num in nums:
        if num not in collection:
            collection.add(num)
    for i in range(1,len(nums)+1):
        if i not in collection:
            missing.append(i)
    return missing

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print findDisappearedNumbers(nums)