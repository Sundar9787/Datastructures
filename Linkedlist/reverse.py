class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SingleLL:
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
     def reverse(self):
        prev = None 
        curr = self.head
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        print("The revesed linked list is :")
        self.head = prev
      def display(self):
        temp = self.head
        while temp:
            print(temp.data, end ="->")
            temp = temp.next
        print("None")
        
sll = SingleLL()
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.display()
sll.reverse()
sll.display()
        
