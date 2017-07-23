#!/usr/bin/python
# This program finds the max element in a binary tree without recursion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_bt_iterative(root):
    if not root:
        return
    maxx = -float("infinity")
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        if front.val > maxx:
            maxx = front.val
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
    return maxx

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print max_bt_iterative(root)
