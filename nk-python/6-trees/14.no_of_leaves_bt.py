#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the number of leaves in a binary tree

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def number_of_leaves(root):
    if not root:
        return 0
    leaves = 0
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        if front.left is None and front.right is None:
            leaves += 1
        else:
            if front.left:
                q.put(front.left)
            if front.right:
                q.put(front.right)
    return leaves


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print number_of_leaves(root)

