#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the size (no of nodes) of a binary tree without recursion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bt_size(root):
    if not root:
        return 0
    q = Queue.Queue()
    q.put(root)
    size = 0
    while not q.empty():
        front = q.get()
        size += 1
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
    return size

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print bt_size(root)

