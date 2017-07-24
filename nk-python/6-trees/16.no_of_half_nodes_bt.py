#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the number of half nodes in a binary tree using recursion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def number_of_half_nodes(root):
    if not root:
        return 0
    x = 0
    if (root.left and root.right is None) or (root.left is None and root.right):
        x = 1
    return number_of_half_nodes(root.left) + number_of_half_nodes(root.right) + x

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print number_of_half_nodes(root)

