## FIFO
from collections import deque

queue = deque([])

queue.append(10)   
queue.append(20)
queue.append(30)

print(list(queue)) ### [10,20,30]

print(queue.popleft())

print(list(queue))
