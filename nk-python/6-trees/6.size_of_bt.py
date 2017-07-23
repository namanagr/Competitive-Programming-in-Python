#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the size (no of nodes) of a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bt_size(root):
    if not root:
        return 0
    return bt_size(root.left) + bt_size(root.right) + 1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print bt_size(root)

