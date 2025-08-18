# To implement a circular queue in Python, we can use a list to represent the queue 
# and manage the front and rear indices.
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]
