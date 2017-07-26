#!/usr/bin/python
# This program constructs a binary tree from inorder and preorder tree traversal.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_bt(preorder, inorder):
    if inorder:
        root = TreeNode(preorder.pop(0))
        inorder_root_index = inorder.index(root.val)
        root.left = construct_bt(preorder, inorder[:inorder_root_index-1])
        root.right = construct_bt(preorder, inorder[inorder_root_index + 1:])
        return root

def preorder_traversal(root):
    if not root:
        return
    print root.val
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print root.val
    inorder_traversal(root.right)

if __name__ == "__main__":
    preorder = [1,2,3,4,5]
    inorder = [2,1,4,3,5]

    preorder = [4,2,5,1,6,3]
    inorder = [1,2,4,5,3,6]
    root = construct_bt(preorder, inorder)
    print "preorder traversal.."
    preorder_traversal(root)
    print "inorder traversal.."
    inorder_traversal(root)


