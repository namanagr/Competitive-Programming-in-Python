#!/usr/bin/python
# This program finds the sum of all the elements in the binary tree
# Author : Naman Agrawal


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_bt(root):
    if not root:
        return 0
    return sum_bt(root.left) + sum_bt(root.right) + root.val

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print sum_bt(root)