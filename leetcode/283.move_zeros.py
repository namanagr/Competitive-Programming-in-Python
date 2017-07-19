#!/usr/bin/python
#Move zeros

def move_zeros(nums): # Less optimized
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1
    return nums

def move_zeros_opt(nums): # Optimized solutions
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    #print move_zeros(nums)
    print move_zeros_opt(nums)