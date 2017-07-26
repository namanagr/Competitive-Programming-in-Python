#!/usr/bin/python
# This program finds if two trees are mirrors of each other

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mirrors(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    elif root1.val != root2.val:
        return False
    else:
        return mirrors(root1.left, root2.right) and mirrors(root1.right, root2.left)

if __name__ == "__main__":
    #Tree1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    #Tree2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.left = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.left.left = TreeNode(10)
    print mirrors(root,root2)
