class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Base case: if root is None, return None
        if root is None:
            return
        
        # Recursively mirror the left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        
        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left
