#!/usr/bin/python
#Delte node in a singly linked list

from linkedlist import *

class LList(LinkedList):
    def delete(self,val):
        if self.head == None:
            return
        temp = self.head
        prev = None
        while temp != None:
            if temp.data == val:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

if __name__ == "__main__":
    ll = LList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.delete(3)
    ll.printll()
