#!/usr/bin/python
#This program finds a number in a binary tree without recursion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_search(root, item):
    if root is None:
        return False
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        if front.val == item:
            return True
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
    return False

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print binary_search(root, 4)
