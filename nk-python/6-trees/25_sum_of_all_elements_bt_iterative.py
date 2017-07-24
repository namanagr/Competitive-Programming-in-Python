#!/usr/bin/python
# This program finds the sum of all the elements in the binary tree without recursion
# Author : Naman Agrawal

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_bt(root):
    if not root:
        return 0
    q = Queue.Queue()
    q.put(root)
    sum = 0
    while not q.empty():
        front = q.get()
        sum += front.val
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
    return sum

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print sum_bt(root)