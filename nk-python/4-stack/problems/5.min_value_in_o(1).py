#!/usr/bin/python
# Implement a program that always gives you the min value int the reamining stack in 0(1) time.

from stacklist import *

class SmartStack:
    def __init__(self):
        self.stk = Stack()
        self.min = Stack()

    def push(self, data):
        self.stk.push(data)
        if self.min.isEmpty() or data <= self.min.peek():
            self.min.push(data)
        else:
            self.min.push(self.min.peek())

    def min_val(self):
        return self.min.peek()

    def pop(self):
        self.min.pop()
        return self.stk.pop()

if __name__ == "__main__":
    s1 = SmartStack()
    s1.push(2)
    s1.push(6)
    s1.push(4)
    s1.push(1)
    s1.push(5)
    print s1.min_val()
    s1.pop()
    s1.pop()
    print s1.pop()
    print s1.min_val()
