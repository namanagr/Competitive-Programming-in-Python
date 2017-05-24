#!/usr/bin/python
'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

from linkedlist import *

class LList(LinkedList):

    def add_two_nums(self, num1, num2):
        size1 = num1.getLength()
        size2 = num2.getLength()
        pad_num1 = 0
        pad_num2 = 0
        if size1 > size2:
            pad_num2 = size1 - size2
        elif size2 > size1:
            pad_num1 = size2 - size1


    def getLength(self):
        length = 0
        temp = self.head
        while temp != None:
            length += 1
            temp = temp.next
        return length

if __name__ == "__main__":
    num1 = LList()
    num1.append(7)
    num1.append(2)
    num1.append(4)
    num1.append(3)
    #print num1.getLength()
    print "Printing num1.."
    num1.printll()
    num2 = LList()
    num2.append(5)
    num2.append(6)
    num2.append(4)
    #print num2.getLength()
    print "Printing num2.."
    num2.printll()
