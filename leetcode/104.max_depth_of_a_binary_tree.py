#!/usr/bin/python
#Find the maximum depth of a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(root):
    if root is None:
        return 0
    else:
        return max(maxDepth(root.left),maxDepth(root.right)) + 1

if __name__ == "__main__":
    # Driver Program
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print maxDepth(root)