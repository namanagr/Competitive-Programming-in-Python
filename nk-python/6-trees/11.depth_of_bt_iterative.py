#!/usr/bin/python
# Author: Naman Agrawal
# This program finds the depth of a binary tree without recursion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_bt(root):
    if not root:
        return 0
    q = Queue.Queue()
    height = 0
    q.put(root)
    while True:
        nodecount = q.qsize()
        if nodecount == 0:
            break
        height += 1
        while nodecount > 0:
            front = q.get()
            if front.left:
                q.put(front.left)
            if front.right:
                q.put(front.right)
            nodecount -= 1
    return height

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print depth_bt(root)

