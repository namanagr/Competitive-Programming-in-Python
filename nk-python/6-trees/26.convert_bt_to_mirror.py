#!/usr/bin/python
# This program converts a binary tree to its mirror.
# Author : Naman Agrawal

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mirror(root):
    if not root:
        return
    mirror(root.left)
    mirror(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    mirror(root)
