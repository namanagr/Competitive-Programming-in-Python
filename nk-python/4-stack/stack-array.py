#!/usr/bin/python
# Implementation of stack using arrays

class Stack:

    def __init__(self):
        self.top = -1
        #self.stack = [0]*20
        self.stack = []

    def isEmpty(self):
        return self.top == -1

    def push(self, data):
        self.top += 1
        #self.stack[self.top] = data
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print "Unable to pop since stack is empty."
            return
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        return self.stack[self.top]

if __name__ == "__main__":
    stack = Stack()
    print "Pushing 4 items to the stack.."
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print "Popping 2 items from the stack.."
    print stack.pop()
    print stack.pop()
    print "Printing the current top item on the stack.."
    print stack.peek()

