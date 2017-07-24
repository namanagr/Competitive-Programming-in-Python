#!/usr/bin/python
# This program finds the diameter of a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth(root):
    if not root:
        return 0
    return max(depth(root.left), depth(root.right)) + 1

def diameter_bt(root):
    if not root:
        return 0
    left_height = depth(root.left)
    right_height = depth(root.right)
    left_diameter = diameter_bt(root.left)
    right_diameter = diameter_bt(root.right)
    return max((left_height + right_height + 1), max(left_diameter, right_diameter))

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print diameter_bt(root)
