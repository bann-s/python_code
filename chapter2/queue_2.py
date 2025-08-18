# 5. Real-world example: Task processing
print("\n=== Real-world Example: Task Processor ===")

def worker(task_queue, worker_id):
    """Worker function that processes tasks from queue"""
    while True:
        try:
            # Get task with timeout
            task = task_queue.get(timeout=1)
            print(f"Worker {worker_id} processing: {task}")
            time.sleep(0.5)  # Simulate work
            task_queue.task_done()
        except:
            break

# Create task queue
task_queue = Queue()

# Add tasks
tasks = ["Send email", "Process data", "Generate report", "Backup files"]
for task in tasks:
    task_queue.put(task)

# Create and start worker threads
threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(task_queue, i+1))
    t.daemon = True
    t.start()
    threads.append(t)

# Wait for all tasks to complete
task_queue.join()
print("All tasks completed!")

print("\n=== Common Use Cases ===")
print("""
1. **Task Processing**: Distribute work among multiple workers
2. **Producer-Consumer**: One thread produces data, another consumes
3. **Breadth-First Search**: Graph/tree traversal algorithms
4. **Print Queue**: Managing print jobs
5. **Web Scraping**: Queue URLs to scrape
6. **Message Passing**: Communication between processes
7. **Buffering**: Smooth data flow between fast producer and slow consumer
""")

# 6. Simple custom queue implementation
print("\n=== Custom Queue Implementation ===")
class SimpleQueue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove item from front of queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        """Look at front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

# Test custom queue
custom_q = SimpleQueue()
custom_q.enqueue("First")
custom_q.enqueue("Second")
print(f"Front item: {custom_q.peek()}")
print(f"Queue size: {custom_q.size()}")
print(f"Dequeued: {custom_q.dequeue()}")
print(f"Queue size after dequeue: {custom_q.size()}")