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

def nextGreaterElement(self, findNums, nums): # More optimized
    output = []
    map = {}
    for i in range(len(nums)):
        map[nums[i]] = i
    for item in findNums:
        pos = map[item]
        val = -1
        for i in range(pos + 1, len(nums)):
            if nums[i] > item:
                val = nums[i]
                break
        output.append(val)
    return output


def findNextGreaterNo(findNums, nums): # Most optimized solution
    st = []
    map = {}
    output = []
    for item in nums:
        while len(st) > 0 and st[-1] < item:
           map[st.pop()] = item
        st.append(item)
    for item in findNums:
        output.append(map.get(item,-1))
    return output

def naman_code(findNums, nums): # Personalized best solution
    output = []
    map = {}
    # Create a mapping of next greatest element of each element of nums array
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                map[nums[i]] = nums[j]
                break

    # Parsing findNums and generating the output array
    for item in findNums:
        if item in map:
            output.append(map[item])
        else:
            output.append(-1)
    return output



nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums3 = [2,4]
nums4 = [1,2,3,4]
print findNextGreaterNo(nums1, nums2)
print findNextGreaterNo(nums3, nums4)
print naman_code(nums1, nums2)
print naman_code(nums3, nums4)