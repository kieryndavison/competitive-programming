"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return 
        
        # Define globa variables to hold the head and prev values
        self.head = None
        self.prev = None
        
        # Perform in order traversal on the tree and update the left and right pointers
        def inOrderTraversal(node):
            if not node: return 
            
            inOrderTraversal(node.left)
            if self.prev: 
                self.prev.right, node.left = node, self.prev
            else: self.head = node
            self.prev = node
            inOrderTraversal(node.right)
        
        inOrderTraversal(root)

        # Connect the last node in the list to the head node to make the list circular
        self.head.left, self.prev.right = self.prev, self.head
        return self.head