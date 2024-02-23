#Stacks and Queues:
class Stack:
    def __init__(self) -> None:
        self.item = []
    
    def push(self,item):
        self.item.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
    
    def is_empty(self):
        return len(self.item) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        
    def display(self):
        for i in self.item:
            print(i)
        

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        
c1 = Stack()
c1.push(7)
c1.push(8)
c1.push(9)
c1.pop()
c1.display()
