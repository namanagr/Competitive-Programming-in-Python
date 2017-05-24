#!/usr/bin/python

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

from linkedlist import *

class LList(LinkedList):
    def add_nums(self,n1,n2):
        temp1 = n1.head
        temp2 = n2.head
        if not temp1 and not temp2:
            return 0
        if not temp1:
            return n2
        if not temp2:
            return temp1
        carry = 0
        while temp1 != None or temp2 != None or carry != 0:
            total = 0
            if temp1:
                total += temp1.data
                temp1 = temp1.next
            if temp2:
                total += temp2.data
                temp2 = temp2.next
            total += carry
            self.append(total%10)
            carry = total/10

if __name__ == "__main__":
    num1 = LList()
    num2 = LList()
    num3 = LList()
    num1.append(8)
    num1.append(8)
    num1.append(9)
    print "Printing the first number.."
    num1.printll()
    num2.append(9)
    num2.append(9)
    num2.append(8)
    print "Printing the second number.."
    num2.printll()
    num3.add_nums(num1,num2)
    print "Printing the sum of the numbers.."
    num3.printll()

'''
#Leetcode working code

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return 0
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        root = l3 = ListNode(0)
        while l1 != None or l2 != None or carry != 0:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            total += carry
            l3.next = ListNode(total%10)
            carry = total/10
            l3 = l3.next
        return root.next
'''
