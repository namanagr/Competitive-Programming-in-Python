#!/usr/bin/python
# Given sum, find a path from root that matches that.
# Author : Naman Agrawal

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pathExplorer(root, providedSum, currentSum):
    if not root:
        return providedSum == currentSum
    currentSum += root.val
    left = pathExplorer(root.left, providedSum, currentSum)
    right = pathExplorer(root.right, providedSum, currentSum)
    return left | right

def hasSum(root, providedSum):
    if not root:
        return False
    return pathExplorer(root, providedSum, 0)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print hasSum(root,7)