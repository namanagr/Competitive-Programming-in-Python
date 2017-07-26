#!/usr/bin/python
# This program finds the level in a binary tree that has max sum

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_max_sum(root):
    if not root:
        return 0
    q = Queue.Queue()
    q.put(root)
    max_sum = float("-infinity")
    max_level = 0
    level = 1
    while True:
        nodecount = q.qsize()
        if nodecount == 0:
            break
        sum = 0
        while nodecount > 0:
            front = q.get()
            sum += front.val
            if front.left:
                q.put(front.left)
            if front.right:
                q.put(front.right)
            nodecount -= 1
        if sum > max_sum:
            max_sum = sum
            max_level = level
        level += 1
    return max_level


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print level_max_sum(root)
