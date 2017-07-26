#!/usr/bin/python
# This program traverses the nodes of a binary tree in a zigzag fashion

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigzag_traversal(root):
    if not root:
        return


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    zigzag_traversal(root)

