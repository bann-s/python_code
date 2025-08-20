#Breadth First Search
# Level of a Node in Binary Tree using BFS
# Given a Binary Tree and a key, the task is to find the level of key in the Binary Tree.
# Iteration 


from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findLevel(root, key):
    if root is None:
        return -1
    # Using iterative approach with a queue
    queue = deque([(root, 1)])  # (node, level) 
    
    while queue:
        current_node, level = queue.popleft()
        
        if current_node.val == key:
            return level
        
        if current_node.left is not None:
            queue.append((current_node.left, level + 1))
        
        if current_node.right is not None:
            queue.append((current_node.right, level + 1))
    
    return -1  # key not found

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Creating a sample binary tree:
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7

    key = 2
    level = findLevel(root, key)
    
    if level != -1:
        print(f"Level of node with key {key} is: {level}")
    else:
        print(f"Node with key {key} not found in the tree.")