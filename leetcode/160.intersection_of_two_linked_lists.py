#!/usr/bin/python
# Returns the node which is the intersection node of two linked lists
# Built in leetcode. Need to modify the program to run in IDE

'''
class Solution(object): # Using hashmap - less optimized
    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB
        map = {}
        while temp1 != None:
            map[temp1] = 1
            temp1 = temp1.next
        while temp2 != None:
            if temp2 in map:
                return temp2
            temp2 = temp2.next
        return None
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def getIntersectNode(headA, headB):
    if headA is None or headB is None:
        return None
    len1 = 0
    temp1 = headA
    while temp1: # Calculate the length of headA
        len1 += 1
        temp1 = temp1.next
    len2 = 0
    temp2 = headB # Calculate the length of headB
    while temp2:
        len2 += 1
        temp2 = temp2.next
    diff = abs(len1 - len2) # Calculate the difference in length
    if len1 > len2:
        temp1 = headA
        temp2 = headB
    else:
        temp1 = headB
        temp2 = headA

    for i in range(diff):
        temp1 = temp1.next

    while temp1:
        if temp1 == temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next
    return None

if __name__ == "__main__":
    headA = ListNode(0)
    headA.next = ListNode(1)
    headA.next.next = ListNode(2)
    headA.next.next.next = ListNode(3)
    headB = ListNode(10)
    headB.next = ListNode(11)
    headB.next.next = headA.next.next
    intersectingNode = getIntersectNode(headA, headB)
    if intersectingNode is not None:
        print "The lists intersect at ", intersectingNode.val
    else:
        print "The lists do not intersect"
