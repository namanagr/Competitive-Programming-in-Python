# Swap two given nodes of a linked list without swapping data

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def push(self, element):
        new_node = Node(element)
        temp = self.head
        self.head = new_node
        self.head.next = temp
        
    def append(self, element):
        new_node = Node(element)
        temp = self.head
        if self.head == None:
            self.head = new_node
            print "first node added"
            return
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        print "next node added"
    
    def print_llist(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next
    
    def swap(self, x, y):
        # case1 - both are equal 
        if x == y:
            return 1
        
        prevX = None
        curX = self.head
        # Search the location of x and store prev and current node
        while curX:
            if curX.data == x:
                break
            prevX = curX
            curX = curX.next
            
        prevY = None
        curY = self.head
        # Search the location of y and store prev and current node
        while curY:
            if curY.data == y:
                break
            prevY = curY
            curY = curY.next
            
        if curX == None or curY == None:
            return 1
        
        if prevX != None:
            prevX.next = curY
        else:
            self.head = curY
            
        if prevY != None:
            prevY.next = curX
        else:
            self.head = curX
            
        temp = curX.next
        curX.next = curY.next
        curY.next = temp
        
    def reverse(self):
       
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.print_llist()
    llist.reverse()
    llist.print_llist()