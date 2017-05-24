#!/usr/bin/python
# Post-order Tree Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printpreorder(root):
    if root:
        print root.data
        printinorder(root.left)
        printinorder(root.right)

def printinorder(root):
    if root:
        printinorder(root.left)
        print root.data
        printinorder(root.right)

def printpostorder(root):
    if root:
        printinorder(root.left)
        printinorder(root.right)
        print root.data

def findmax(root)
    maxData = float("-infinity")


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print "Preorder tree traversal.."
    printpreorder(root)
    print "Inorder tree traversal.."
    printinorder(root)
    print "Postorder tree traversal.."
    printpostorder(root)
