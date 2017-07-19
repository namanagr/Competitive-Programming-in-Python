#!/usr/bin/python
# This program returns the array of next greater number for all elements in the array.

def nextGreaterNo(findNums, nums):
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

if __name__ == "__main__":
    nums = [1,3,4,2]
    findNums = [4,1,2]
    print nextGreaterNo(findNums, nums)