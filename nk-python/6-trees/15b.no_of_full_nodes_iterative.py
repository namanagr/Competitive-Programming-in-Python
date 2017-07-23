#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the number of full nodes in a binary tree

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def number_of_full_nodes(root):
    if not root:
        return 0
    fullnodes = 0
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        if front.left and front.right:
            fullnodes += 1
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
    return fullnodes

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print number_of_full_nodes(root)

