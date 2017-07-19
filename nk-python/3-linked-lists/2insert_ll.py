# Insert elements into the linked list

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__ (self):
        self.head = None
    
    def push(self, element):
        if self.head == None:
            self.head = Node(element)
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            new_node = Node(element)
            temp.next = new_node
    
    def insert(self, element, pos):
        new_node = Node(element)
        if pos == 1:
            new_node.next = self.head
            return 0
        temp = self.head
        current_pos = 1
        while(pos > current_pos):
            prev = temp
            if temp == None:
                return 1
            temp = temp.next
            current_pos += 1
        new_node.next = temp
        prev.next = new_node
        return 0
    
    def delnode_element(self, element):
        if element == self.head.data:
            self.head = self.head.next
            return 0
        temp = self.head
        flag = 0
        while(temp):
            if temp.data == element:
                flag = 1
                break
            prev = temp
            temp = temp.next
        if flag == 1:
            prev.next = temp.next
            return 0
        else:
            return 1
            
    def delnode_pos(self, pos):
        if pos == 1:
            self.head = self.head.next
            return 0
        temp = self.head
        current_pos = 1
        flag = 0
        while pos > current_pos:
            if temp == None:
                return 1
            prev = temp
            temp = temp.next
            current_pos += 1
        prev.next = temp.next
        return 0
        
    def print_llist(self):
        temp = self.head
        print "Elements of the linked list - "
        while(temp):
            print temp.data
            temp = temp.next
            
if __name__ == "__main__":
    llist = LinkedList()
    num = input("Enter number of elements to be added to the linked list: ")
    i=1
    while(i <= num):
        element = input("Enter element " + str(i) + ": ")
        llist.push(element)
        i += 1
    llist.print_llist()
    llist.delnode_pos(6)        
    llist.print_llist()
    
    