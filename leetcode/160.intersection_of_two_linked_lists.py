#!/usr/bin/python
# Returns the node which is the intersection node of two linked lists
# Built in leetcode. Need to modify the program to run in IDE

class Solution(object):
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