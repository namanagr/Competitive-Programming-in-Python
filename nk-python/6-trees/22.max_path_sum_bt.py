#!/usr/bin/python
# This program finds the max path dum in a given binary tree.
# The path may start or end at any node of the binary tree.
# Author : Naman Agrawal

total_sum = 0

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_sum_compute(root):
    if not root:
        return 0
    l = path_sum_compute(root.lef t)
    r = path_sum_compute(root.right)
    temp1 = max(max(l,r),root.val)
    temp2 = max(temp1, l+r+root.val)
    path_sum_compute.res = max(path_sum_compute.res, temp2)
    return temp2

def max_path_sum(root):
    path_sum_compute.res = float("-infinity")
    path_sum_compute(root)
    return path_sum_compute.res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print max_path_sum(root)