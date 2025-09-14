# Python program for insertion and deletion in Circular Queue
class Queue:
    def __init__(self, c):
        self.arr = [0] * c
        self.capacity = c
        self.size = 0
        self.front = 0
        print(f"Queue initialized with capacity {c}")
        self._print_state()

    def _print_state(self):
    #"""Helper method to print the current state of the queue"""
        print(f"Array: {self.arr}")
    
    # Create visual representation showing only active queue elements
        visual = ['_'] * self.capacity
        if self.size > 0:
            for i in range(self.size):
                pos = (self.front + i) % self.capacity
                visual[pos] = str(self.arr[pos])
    
        print(f"Active: {visual}")  # Shows which positions are actually in use
        print(f"Front: {self.front}, Size: {self.size}, Capacity: {self.capacity}")
    
        if self.size > 0:
            rear = (self.front + self.size - 1) % self.capacity
            print(f"Front element: {self.get_front()}, Rear element: {self.get_rear()}")
        else:
            print("Queue is empty")
        print("-" * 40)

    # Get the front element
    def get_front(self):
        """Return the front element of the queue"""
        if self.size == 0:
            return -1
        return self.arr[self.front]

    # Get the rear element
    def get_rear(self):
        """Return the rear element of the queue"""
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.arr[rear]

    # Insert an element at the rear
    def enqueue(self, x):
        """Add element to the rear of the queue"""
        print(f"Enqueuing {x}:")
        if self.size == self.capacity:
            print(f"Queue is full! Cannot enqueue {x}")
            return
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1
        self._print_state()

    # Remove an element from the front
    def dequeue(self):
        """Remove and return element from front of the queue"""
        print("Dequeue operation:")
        if self.size == 0:
            print("Queue is empty, cannot dequeue")
            self._print_state() 
            return -1
        
        res = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued element: {res}")
        self._print_state()
        return res

if __name__ == '__main__':
    q = Queue(4)
    
    # Test enqueue operations
    q.enqueue(10)
    print(f"Front: {q.get_front()}, Rear: {q.get_rear()}\n")
    
    q.enqueue(20)
    print(f"Front: {q.get_front()}, Rear: {q.get_rear()}\n")
    
    q.enqueue(30)
    print(f"Front: {q.get_front()}, Rear: {q.get_rear()}\n")
    
    q.enqueue(40)
    print(f"Front: {q.get_front()}, Rear: {q.get_rear()}\n")
    
    # Test dequeue operations
    q.dequeue()
    print(f"Front: {q.get_front()}, Rear: {q.get_rear()}\n")
    
    q.dequeue()
    print(f"Front: {q.get_front()}, Rear: {q.get_rear()}\n")
    
    # Test circular behavior
    q.enqueue(50)
    print(f"Front: {q.get_front()}, Rear: {q.get_rear()}")