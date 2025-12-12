class Stack:
    def __init__(self): 
        self.items = [] # creates an empty stacks     
    
    def push(self, item):
        self.items.append(item)   
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()  
    
    # peek shows top element
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]     
    
    def is_empty(self):
        return len(self.items) == 0  
    
    def size(self):
        return len(self.items)        
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.items) # 10, 20, 30
stack.pop() # 30

print("After pop:", stack.items) # 10 , 20 
print("Top element:", stack.peek())  # 20
print("Stack empty?", stack.is_empty()) # no 
print("Stack size:", stack.size()) # lengthS
