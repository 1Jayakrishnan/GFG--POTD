class Solution:
    def findMaxForN(self, root, n):
        # Initialize the result variable to store the maximum value
        result = -1
        
        # Traverse the BST
        while root:
            # If the current node value is less than or equal to n, update the result
            if root.key <= n:
                result = max(result, root.key)
                # Move to the right subtree to find a greater value
                root = root.right
            # If the current node value is greater than n, move to the left subtree
            else:
                root = root.left
        
        # Return the result
        return result
        
