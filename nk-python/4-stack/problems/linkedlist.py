#!/usr/bin/python
#List list class and methods to be inherited

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def printll(self):
        if self.head == None:
            print "Empty Linked List"
        else:
            temp = self.head
            while temp != None:
                print temp.data
                temp = temp.next

'''
if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    ll1.append(5)
    ll1.printll()
    ll1.reverse()
    print "Printing the reversed linked list"
    ll1.printll()
'''
