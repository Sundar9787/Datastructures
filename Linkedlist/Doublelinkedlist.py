class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedlist:
    def __init__(self):
        self.head = None
        
    
    def insert(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
                
            temp.next = new_node
            new_node.prev = temp
            
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->")
            temp = temp.next
        print("None")
        
    def display_backward(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data,end="<->")
            temp = temp.prev
        print("None")
        
ddl= DoubleLinkedlist()
ddl.insert(1)
ddl.insert(2)
ddl.insert(3)
ddl.display_forward()
ddl.display_backward()
        
