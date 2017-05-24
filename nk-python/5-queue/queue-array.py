#!/usr/bin/python
# Implemtation of queue using arrays

class Queue:

    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.queue = [0]*size
        self.size = size

    def enqueue(self, data):
        if self.front == -1 and self.rear == -1:
            self.rear = 0
            self.front = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print "Can't dequeue.. Empty queue.."
            return -1
        else:
            temp = self.front
            item = self.queue[temp]
            self.front = (self.front + 1) % self.size
            return item

    def print_queue(self):
        temp = self.front
        while True:
            print self.queue[temp]
            if temp == self.rear:
                break
            temp = (temp + 1) % self.size

if __name__ == "__main__":

    queue = Queue(10)
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




