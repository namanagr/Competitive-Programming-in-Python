#!/usr/bin/python
# This program finds the maximum element in a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

max_num = float("-infinity")

def findMax(root):
    if root is None:
        return max_num
    lmax = findMax(root.left)
    rmax = findMax(root.right)
    return max(lmax,root.val,rmax)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print findMax(root)
