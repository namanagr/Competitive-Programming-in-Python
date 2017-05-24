#!/usr/bin/python
# Check whether the given string is a palindrome or not
# Input is given in the form of a linked list

from stacklist import *

def ispalindrome(arr_n):
    if arr_n == None or arr_n.next == None:
        return True
    slow = arr_n
    fast = arr_n
    prev = None

    while not fast.next and not fast.next.next: #Reverse the first half and get to the middle element
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        fast = fast.next.next

    # Check if the list has even / odd number of elements
    if not fast.next: # Condition of odd length
        slow = slow.next
    else:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    while not prev and not slow:
        if prev.data != slow.data:
            return False
        prev = prev.next
        slow = slow.next
    return True

if __name__ == "__main__":
    sent = "naman1"
    arr_node = Node(sent[0])
    to_be_used = arr_node
    for i in range(1,len(sent)):
        arr_node.next = Node(sent[i])
        arr_node = arr_node.next
    print ispalindrome(to_be_used)

