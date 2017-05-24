#!/usr/bin/python
#Check if the elements of a sigly linked list form a palidrome

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    def printll(self):
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            print temp.data
            temp = temp.next

    @property
    def palindrome(self):
        if self.head == None or self.head.next == None:
            return True
        slow = self.head
        fast = self.head
        prev = None
        while True:
            if fast.next != None:
                if fast.next.next != None:
                    # slow pointer moving ahead while reversing first half of the linked list
                    temp2 = slow.next
                    slow.next = prev
                    prev = slow
                    slow = temp2
                    fast = fast.next.next
        if fast.next is None:
            #Odd number of nodes
            mid = prev
        else:
            slow.next = prev
            mid = slow
        half_ahead = slow.next
        while half_ahead != None:
            if half_ahead.data != mid.data:
                return False
            half_ahead = half_ahead.next
            mid = mid.next
        return True

if __name__ == "__main__":
    ll1 = LL()
    ll1.append('a')
    ll1.append('b')
    ll1.append('c')
    ll1.append('b')
    ll1.append('a')
    print ll1.palindrome
