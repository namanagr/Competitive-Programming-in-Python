#!/usr/bin/python
#Given two array of numbers where the first one is the subset of the second
#It returns the next greatest number

def findNextGreatest(num1, num2): #Unoptimized code - n^2 time complexity

    output = []
    for item in num1:
        flag = 0
        for i in range(len(num2)):
            if num2[i] == item:
                if i+1 != len(num2):
                    for j in range(i+1,len(num2)):
                        if num2[j] > item:
                            output.append(num2[j])
                            flag = 1
                            break
                if flag == 0:
                    output.append(-1)
                    break
    return output

nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums3 = [2,4]
nums4 = [1,2,3,4]
print findNextGreatest(nums1, nums2)
print findNextGreatest(nums3, nums4)