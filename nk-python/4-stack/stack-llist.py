#/usr/bin/python
# Stack implementation using LinkedLists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            print "Pop failed. Empty Stack.."
            return -1
        temp = self.head
        self.head = self.head.next
        item = temp.data
        del temp
        return item

    def peek(self):
        if self.head == None:
            print "Peek failed. Empty Stack.."
            return -1
        return self.head.data

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
