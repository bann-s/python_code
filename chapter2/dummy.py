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
        """Helper method to print the current state of the queue"""
        print(f"Array: {self.arr}")
        print(f"Front: {self.front}, Size: {self.size}, Capacity: {self.capacity}")
        if self.size > 0:
            rear = (self.front + self.size - 1) % self.capacity
            print(f"Front element: {self.get_front()}, Rear element: {self.get_rear()}")
        else:
            print("Queue is empty")
        print("-" * 40)

    # Get the front element
    def get_front(self):  # Changed from getFront
        """Return the front element of the queue"""
        if self.size == 0:
            return -1
        return self.arr[self.front]

    # Get the rear element
    def get_rear(self):  # Changed from getRear
        """Return the rear element of the queue"""
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.arr[rear]

    # Insert an element at the rear
    def enqueue(self, x):
        """Add element to the rear of the queue"""
        if self.size == self.capacity:
            print(f"Queue is full! Cannot enqueue {x}")
            return
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1
        print(f"Enqueued: {x}")
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
        self._print_state()
        print(f"Dequeued element: {res}")   
        return res

if __name__ == '__main__':
    q = Queue(4)
    q.enqueue(10)
    print(q.get_front(), q.get_rear())  # Updated method calls
    q.enqueue(20)
    print(q.get_front(), q.get_rear())  # Updated method calls
    q.enqueue(30)
    print(q.get_front(), q.get_rear())  # Updated method calls
    q.enqueue(40)
    print(q.get_front(), q.get_rear())  # Updated method calls
    q.dequeue()
    print(q.get_front(), q.get_rear())  # Updated method calls
    q.dequeue()
    print(q.get_front(), q.get_rear())  # Updated method calls
    q.enqueue(50)
    print(q.get_front(), q.get_rear())  # Updated method calls