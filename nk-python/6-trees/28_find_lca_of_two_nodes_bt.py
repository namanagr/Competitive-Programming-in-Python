#!/usr/bin/python
# This program finds the Least Common Ancestor (LCA) of two nodes in a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca (root, root1, root2):
    if not root:
        return None
    if root.val == root1.val or root.val == root2.val:
        return root
    left = lca(root.left, root1, root2)
    right = lca(root.right, root1, root2)
    if left and right: # both nodes are on different sides of root, then lca is root
        return root
    else:
        if left:
            return left
        else:
            return right

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(10)
    print lca(root, root.left, root.left.left).val
