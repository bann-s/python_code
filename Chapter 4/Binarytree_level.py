#Level of a Node in Binary Tree     #DEPTH FIRST SEARCH
#Given a Binary Tree and a key, the task is to find the level of key in the Binary Tree.
#Recursion

#Idea: Start from Root -> If key is found at root then return the root's level. Or Recursively call Left and Right subtrees with level+1. If the key is found, return the level of the node, otherwise return -1.#Time Complexity: O(n), where n is the number of nodes in the tree.
#Space Complexity: O(h), where h is the height of the tree due to recursion stack.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findLevel(root, key, level=1):
    if root is None:
        return -1
    
    if root.val == key: #if key is found at root
        return level
    
    left_level = findLevel(root.left, key, level + 1) #first check left subtree
    if left_level != -1:
        return left_level
    
    return findLevel(root.right, key, level + 1)  # if not found in left subtree, check right subtree

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

    key = 1
    level = findLevel(root, key)
    
    if level != -1:
        print(f"Level of node with key {key} is: {level}")
    else:
        print(f"Node with key {key} not found in the tree.")
    


