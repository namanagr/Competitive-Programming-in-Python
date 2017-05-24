#!/usr/bin/python
#Remove duplicates from a sorted array
#No extra memory usage
#Return length after removing duplicates

def removedup(nums):
    if nums is None:
        return 0
    index = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
    return index + 1


if __name__ == "__main__":
    nums = [1,1,2]
    print removedup(nums)
