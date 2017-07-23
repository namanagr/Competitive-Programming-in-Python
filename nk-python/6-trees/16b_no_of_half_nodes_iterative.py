#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the number of half nodes in a binary tree

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def number_of_half_nodes(root):
    if not root:
        return 0
    halfnodes = 0
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        if (front.left and front.right is None) or (front.left is None and front.right):
            halfnodes += 1
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
    return halfnodes

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print number_of_half_nodes(root)

