#!/usr/bin/python
# This program finds if two trees are structurally identical or not

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def struc_indetical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        return struc_indetical(root1.left,root2.left) & struc_indetical(root1.right,root2.right)
    else:
        return False

if __name__ == "__main__":
    #Tree1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    #Tree2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.right = TreeNode(15)
    print struc_indetical(root,root2)
