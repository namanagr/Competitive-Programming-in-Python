#!/usr/bin/python
l = [['a', 'b', 'c'], ['a', 'b'], ['g', 'h', 'r', 'w']]
locations = ["p1, p2, p3","p4, p5","p6, p7, p8, p9"]
for i in range(len(locations)):
    locations[i] = locations[i].split(", ")
#print locations
arr = []
def permu(lists, prefix=''):
    if not lists:
        arr.append(prefix)
        return
    first = lists[0]
    rest = lists[1:]
    for letter in first:
        permu(rest, prefix + letter + ",")
permu(locations)
for i in range(len(arr)):
    arr[i] = arr[i][0:len(arr[i])-1]
print arr
