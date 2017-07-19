# merge two sorted linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, element):
        new_node = Node(element)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    
    def print_llist(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next
            
    def merge(self, l1, l2):
        temp1 = l1.head
        temp2 = l2.head
        temp = self.head
        if temp1 == None:
            temp = temp2
        elif temp2 == None:
            temp = temp1
        else:
            while temp1.next != None and temp2.next != None:
                if temp1.data < temp2.data:
                    if temp == None:
                        self.head = Node(temp1.data)
                        temp = self.head
                        print "t1 head"
                    else:
                        temp.next = Node(temp1.data)
                        print "t2 element"
                    temp1 = temp1.next
                else:
                    if temp == None:
                        self.head = Node(temp2.data)
                        temp = self.head
                        print "t2 head"
                    else:
                        temp.next = Node(temp2.data)
                        print "t2 element"
                    temp2 = temp2.next
            #while temp1.next != None and temp2.next == None:
            #    new_node = Node
            
        
if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll3 = LinkedList()
    ll1.append(1)
    ll1.append(5)
    ll1.append(15)
    print "list1 elements are :"
    ll1.print_llist()
    ll2.append(4)
    ll2.append(10)
    ll2.append(20)
    print "list2 elements are :"
    ll2.print_llist()
    ll3.merge(ll1,ll2)
    print "merged list elements :"
    ll3.print_llist()
    
    
    