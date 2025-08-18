#I want to understand how to use queues in Python and its use cases.
#help me implement it in a simple way

# This code demonstrates a basic implementation of a queue in Python using the `queue` module.
# The `Queue` class provides a thread-safe FIFO queue implementation.
# The code adds three items to the queue, processes them in the order they were added, and prints the size of the queue.
# The `put` method adds items to the queue, and the `get` method retrieves and removes items from the queue.
# The `qsize` method returns the number of items in the queue.
# The loop continues until the queue is empty, ensuring all items are processed.

#Queue is a First In First Out (FIFO) data structure
# It is useful for scenarios like task scheduling, managing resources, etc.
# In this example, we added three items to the queue and processed them in the order they were added.
# This demonstrates the basic usage of a queue in Python.# You can also check the size of the queue
# print("Queue size:", q.qsize())

#Queues are objects in memory - reassigning the variable loses the old queue
#Use limit_q.full() to check if queue is at capacity before adding more items

from queue import Queue

# Create a queue
print("Basic Queue Implementation in Python")
q = Queue()

# Add items to the queue
q.put("item1")
q.put("item2")
q.put("item3")
print("\nQueue size:", q.qsize())
# Remove items from the queue
while not q.empty():
    item = q.get()
    print("Processing:", item)

items = ["item1", "item2", "item3"]
for item in items:
    q.put(item)
# Process items in the queue
while not q.empty():
    item = q.get()
    print("Processing:", item)

# Queue with Size limit 
print("\nQueue with size limit\n")
limit_q = Queue(maxsize=5)      # Empty queue, max size 5
limit_q.put("12")               # Queue: ["12"] - size 1
limit_q.put("34")               # Queue: ["12", "34"] - size 2

# Add items to the queue with a size limit
for i in range(2, 4):
    limit_q.put(f"limited_item{i+1}")       # Queue: ["12", "34", "limited_item3"] - size 3
    print(f"Added: limited_item{i+1}, Queue size: {limit_q.qsize()}")
    # Queue: ["12", "34", "limited_item3", "limited_item4"] - size 4


# limit_q = Queue(maxsize=5) # this recreates the same queue instead of adding to it. 
# SO DO NOT CALL THIS AGAIN UNLESS YOU WANT TO RESET THE QUEUE

for i in range(3):                      # i =0,1,2   
    if not limit_q.full():             # Check if the queue is full before adding more items
        limit_q.put(f"more_item{i+1}")   # Queue: ["12", "34", "limited_item3", "limited_item4", "more_item1"] - size 5 
                                            # QUEUE IS FULL! This will BLOCK indefinitely! So  you must put a check if it is full or 
                                            # else the code will hang, it is trying to add more items to a full queue with
                                            # BLOCK=TRUE(default), so it waits forever for the space to become available.
        print(f"Added: more_item{i+1}, Queue size: {limit_q.qsize()}")
    else:
        print("Queue is full")


# PRIORITY QUEUE
from queue import PriorityQueue

pq = PriorityQueue()
# Add items to the priority queue with priorities
pq.put((2, "low_priority_item"))
pq.put((1, "high_priority_item"))
pq.put((3, "medium_priority_item"))

while not pq.empty():
    priority, item = pq.get()
    print(f"Processing: {item} with priority {priority}")