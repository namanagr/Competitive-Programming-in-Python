#!/usr/bin/python
# This program prints all the root to leaf paths in a binary tree

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pathexplorer(root, path1, pathlen):
    if not root:
        return
    path1[pathlen] = root.val
    pathlen += 1
    if not root.left and not root.right:
        p = []
        for i in range(pathlen):
            p.append(path1[i])
        print p
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
    root.right.right = TreeNode(10)
    print all_paths(root)
