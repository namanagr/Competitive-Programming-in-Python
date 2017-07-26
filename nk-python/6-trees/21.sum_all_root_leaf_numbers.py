#!/usr/bin/python
# This program computes all root to leaves numbers and returns their sum

import Queue

total_sum = 0

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pathexplorer(root, path1, pathlen):
    global total_sum
    if not root:
        return
    path1[pathlen] = root.val
    pathlen += 1
    if not root.left and not root.right:
        num = 0
        for i in range(pathlen):
            num = num*10 + path1[i]
        total_sum += num
        #print num
    else:
        pathexplorer(root.left, path1, pathlen)
        pathexplorer(root.right, path1, pathlen)

def all_paths(root):
    if not root:
        return
    path = [0]*1000
    pathexplorer(root, path, 0)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    all_paths(root)
    print total_sum
