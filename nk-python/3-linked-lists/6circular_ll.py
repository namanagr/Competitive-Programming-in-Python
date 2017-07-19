## Program to construct a circular LL and traverse it.

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CirrularLinkedList:
    
    def __init__(self):
        self.head = None
        
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        temp = self.head
        if self.head != None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
        
    def print_ll(self):
        temp = self.head
        while True:
            print temp.data
            temp = temp.next
            if (temp == self.head):
                break
        
if __name__ == "__main__":
    clist = CirrularLinkedList()
    clist.push(5)
    clist.push(6)
    clist.push(7)
    clist.push(8)
    clist.print_ll()