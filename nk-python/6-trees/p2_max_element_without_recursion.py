#!/usr/bin/python
# This program finds the maximum element in a binary tree without recursion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

max_num = float("-infinity")

def findMax(root):
    if root is None:
        return
    global max_num
    q = Queue.Queue()
    q.put(root)
    while (not q.empty()):
        temp = q.get()
        if temp.val > max_num:
            max_num = temp.val
        if temp.left is not None:
            q.put(temp.left)
        if temp.right is not None:
            q.put(temp.right)
    return max_num


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print findMax(root)
