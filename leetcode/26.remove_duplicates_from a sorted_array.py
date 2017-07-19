#!/usr/bin/python
#Remove duplicates from a sorted array
#No extra memory usage
#Return length after removing duplicates


def removeDup(nums):
    if nums == []:
        return 0
    index = 0
    for i in range(1,len(nums)):
        if nums[index] != nums[i]:
            index += 1
            nums[index] = nums[i]
    return index+1


if __name__ == "__main__":
    nums = [1,1,2]
    print removeDup(nums)
