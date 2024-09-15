class Solution:
    def __init__(self):
        self.prev = None  # To keep track of the previous node in DLL
        self.head = None  # To store the head of the DLL

    def bToDLL(self, root):
        # Base case
        if root is None:
            return None
        
        # In-order traversal to convert the tree
        self.convertToDLL(root)
        
        # Return the head of the DLL
        return self.head
    
    def convertToDLL(self, root):
        if root is None:
            return
        
        # Traverse the left subtree
        self.convertToDLL(root.left)
        
        # Process the current node
        if self.prev is None:
            # This node is the leftmost node and becomes the head of the DLL
            self.head = root
        else:
            # Link the previous node (self.prev) with the current node (root)
            root.left = self.prev
            self.prev.right = root
        
        # Update the previous node to the current node
        self.prev = root
        
        # Traverse the right subtree
        self.convertToDLL(root.right)

