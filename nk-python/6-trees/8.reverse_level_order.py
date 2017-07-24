#!/usr/bin/python
# Author: Naman Agrawal
# This program prints the level order in reverse fashion

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelorder_reverse(root):
    if not root:
        return 0
    q = Queue.Queue()
    q.put(root)
    res = []
    st = []
    temp = []
    st.append(root.val)
    while not q.empty():
        front = q.get()
        if front.left:
            q.put(front.left)
            temp.append(front.left.val)
        if front.right:
            q.put(front.right)
            temp.append(front.right.val)
        while temp:
            st.append(temp.pop())
    while st:
        res.append(st.pop())
    return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print levelorder_reverse(root)

