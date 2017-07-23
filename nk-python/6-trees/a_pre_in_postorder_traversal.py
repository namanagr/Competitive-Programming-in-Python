#!usr/bin/python
# Pre order, inorder and postorder traversal of binary tree

import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val

def levelorder(root):
    q = Queue.Queue()
    if root is None:
        return
    q.put(root)
    while not q.empty():
        front = q.get()
        print front.val
        if front.left is not None:
            q.put(front.left)
        if front.right is not None:
            q.put(front.right)

def preorder_iterative(root):
    if root is None:
        return
    st = []
    res = []
    st.append(root)
    while st:
        node = st.pop()
        res.append(node.val)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return res

def inorder_iterative(root):
    if not root:
        return
    st = []
    res = []
    node = root
    while st or node:
        if node:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            res.append(node.val)
            node = node.right
    return res

def postorder_iterative(root):
    if not root:
        return
    st1 = []
    st2 = []
    res = []
    st1.append(root)
    while st1:
        node = st1.pop()
        st2.append(node.val)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
    while st2:
        res.append(st2.pop())
    return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print "preorder traversal.."
    preorder(root)
    print "inorder traversal.."
    inorder(root)
    print "postorder traversal.."
    postorder(root)
    print "levelorder traversal.."
    levelorder(root)
    print "preorder iterative.."
    print preorder_iterative(root)
    print "inorder iterative.."
    print inorder_iterative(root)
    print "postorder iterative.."
    print postorder_iterative(root)
