#!/usr/bin/python
# Author: Naman Agrawal
# This program inserts an element in a binary tree

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelorder_traversal(root):
    if root is None:
        return
    queue = Queue.Queue()
    result = []
    queue.put(root)
    while (not queue.empty()):
        temp = queue.get()
        result.append(temp.val)
        if (temp.left is not None):
            queue.put(temp.left)
        if (temp.right is not None):
            queue.put(temp.right)
    print "Printing the Level Order Traversal.."
    for num in result:
        print num

def bt_insert(root, item):
    if root is None:
        root = TreeNode(item)
    else:
        q = Queue.Queue()
        q.put(root)
        while (not q.empty()):
            temp = q.get()
            if temp.left is None:
                temp.left = TreeNode(item)
                break
            else:
                q.put(temp.left)
            if temp.right is None:
                temp.right = TreeNode(item)
                break
            else:
                q.put(temp.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    bt_insert(root, 7)
    levelorder_traversal(root)


