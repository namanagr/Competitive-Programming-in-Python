#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the number of leaves in a binary tree using recursion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def number_of_leaves(root):
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 1
    return number_of_leaves(root.left) + number_of_leaves(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print number_of_leaves(root)

