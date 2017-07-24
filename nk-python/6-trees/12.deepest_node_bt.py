#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the deepest node

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def deepest_node(root):
    if not root:
        return 0
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
    return front.val


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print deepest_node(root)

