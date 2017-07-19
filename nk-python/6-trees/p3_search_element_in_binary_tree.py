#!/usr/bin/python
# This program searches an element in a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_search(root, item):
    if root is None:
        return False
    if root.val == item:
        return True
    else:
        if binary_search(root.left, item) is True:
            return True
        else:
            return binary_search(root.right, item)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print binary_search(root, 4)
