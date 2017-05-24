#!/usr/bin/python
l = [['a', 'b', 'c'], ['a', 'b'], ['g', 'h', 'r', 'w']]
arr = []
def permu(lists, prefix=''):
    if not lists:
        arr.append(prefix)
        return
    first = lists[0]
    rest = lists[1:]
    for letter in first:
        permu(rest, prefix + letter)
permu(l)
print arr
