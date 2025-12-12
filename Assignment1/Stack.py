### stack using list
### LIFO 

from collections import deque

stack = deque([])

stack.append(10)   
stack.append(20)
stack.append(30)

print(list(stack)) ### [10,20,30]

stack.pop()

print(list(stack))
