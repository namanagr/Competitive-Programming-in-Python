#!/usr/bin/python
# This program returns teh max number of consecutive ones in the input array

def max_consecutive_ones(arr):
    max_count = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    return max(max_count,count)

if __name__ == "__main__":
    arr = [1,1,0,1,1,1]
    print max_consecutive_ones(arr)