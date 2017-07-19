# Implement a double linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DLinked_List:
    def __init__(self):
        self.head = None
    
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node
        
    def append(self, element):
        new_node = Node(element)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def print_dll(self):
         temp = self.head
         while (temp):
             print temp.data
             temp = temp.next
    
if __name__ == "__main__":
    dlist = DLinked_List()
    #dlist.push(4)
    #dlist.push(5)
    #dlist.push(6)
    #dlist.push(7)
    #dlist.push(8)
    dlist.append(1)
    dlist.append(2)
    dlist.append(3)
    dlist.append(4)
    dlist.print_dll()