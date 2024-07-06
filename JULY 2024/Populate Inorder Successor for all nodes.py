class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:

    def __init__(self):
        self.prev = None

    def populateNext(self, root):
        if not root:
            return
        
        # Recursively visit the left subtree
        self.populateNext(root.left)
        
        # Set the next pointer of the previous node to the current node
        if self.prev:
            self.prev.next = root
        
        # Update the previous node to the current node
        self.prev = root
        
        # Recursively visit the right subtree
        self.populateNext(root.right)
