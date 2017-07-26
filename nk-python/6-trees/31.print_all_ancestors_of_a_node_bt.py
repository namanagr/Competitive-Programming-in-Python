#!/usr/bin/python
# This program prints all the ancestors and the element in a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_ancestors(root, node):
    if not root:
        return 0
    if root == node or print_ancestors(root.left, node) or print_ancestors(root.right, node):
        print root.val
        return 1
    return 0

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print_ancestors(root, root.right.right)

