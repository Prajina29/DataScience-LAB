# Queue implementation from scratch
class Queue:
    def __init__(self):
        self.items = []   # internal storage

    def enqueue(self, item): #Add item to the end of the queue
        self.items.append(item)

    def dequeue(self): # Remove item from the front of the queue
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)   # remove first element

    def peek(self): #Check the front element without removing it
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self): #Check if the queue is empty
        return len(self.items) == 0

    def size(self): # Return the number of items in the queue
        return len(self.items)
    
# Using the queue
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:", queue.items)      # [10, 20, 30]
print("Dequeue:", queue.dequeue()) # removes 10
print("After dequeue:", queue.items) # [20, 30]
print("Front element:", queue.peek()) # 20
print("Is empty?", queue.is_empty())  # False
print("Queue size:", queue.size())    # 2

