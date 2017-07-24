#!/usr/bin/python
# This program finds the maximum element in a binary tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_bt(root):
    if root is None:
        return -float("infinity")
    max_left = max_bt(root.left)
    max_right = max_bt(root.right)
    return max(max_left,root.val,max_right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print max_bt(root)