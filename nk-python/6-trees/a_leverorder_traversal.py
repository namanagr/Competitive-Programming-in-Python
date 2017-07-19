#!/usr/bin/python
# Level order traversal of binary tree

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

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    levelorder_traversal(root)