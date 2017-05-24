#!/usr/bin/python
# Implementation of a queue using Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.rear == None:
            new_node = Node(data)
            self.front = new_node
            self.rear = self.front
        else:
            new_node = Node(data)
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front == None:
            print "The queue is empty.."
            return -1
        else:
            temp = self.front
            item = temp.data
            self.front = self.front.next
            return item

    def print_queue(self):
        if self.front == None:
            print "Empty queue.."
        else:
            temp = self.front
            while temp != None:
                print temp.data
                temp = temp.next

if __name__ == "__main__":

    queue = Queue()
    print "Enqueueing 5 numbers.."
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.print_queue()
    print "Dequeueing 5 numbers.."
    print queue.dequeue()
    print queue.dequeue()
    print "Printing the resultant queue.."
    queue.print_queue()

