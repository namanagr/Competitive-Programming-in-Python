#!/usr/bin/python
# This program reverses a Linked List.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    if head == None or head.next == None:
        return head
    temp = head
    prev = None
    temp2 = None
    while temp != None:
        temp2 = temp.next
        temp.next = prev
        prev = temp
        temp = temp2
    return prev

if __name__ == "__main__":
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    print "List Elements.."
    temp = head
    while temp:
        print temp.val
        temp = temp.next
    rev = reverseList(head)
    print "After reversal.."
    while rev:
        print rev.val
        rev = rev.next

