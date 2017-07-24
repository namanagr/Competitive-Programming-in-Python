#!/usr/bin/python
# Author: Naman Agrawal
# This program prints the level order in reverse fashion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def del_bt(root):
    if not root:
        return
    del_bt(root.left)
    del_bt(root.right)
    del root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    del_bt(root)

