# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# For example, Given nums = [0, 1, 3] return 2.
# Note: Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

def missing_no(nums):
    map = {}
    for num in nums:
        if num not in map:
            map[num] = 1
    i = 0
    for key in map:
        if i != key:
            return i
        i += 1
    return i

if __name__ == "__main__":
    nums = [0,3,1]
    #nums = [0]
    nums = [1]

    print missing_no(nums)
