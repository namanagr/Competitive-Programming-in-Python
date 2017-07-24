#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the depth of a binary tree

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_bt(root):
    if not root:
        return 0
    return max(depth_bt(root.left),depth_bt(root.right)) + 1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print depth_bt(root)

