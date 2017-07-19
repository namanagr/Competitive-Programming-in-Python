# Find out the length of a linked list

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
    
    def push (self, element):
        new_node = Node(element)
        temp = self.head
        self.head = new_node
        new_node.next = temp
    
    def print_llist(self):
        temp = self.head
        while (temp):
            print temp.data
            temp = temp.next

    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count
        
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.print_llist()
    print llist.getCount()
    