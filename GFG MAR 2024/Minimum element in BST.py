class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        if not root:
            return None
        
        # Traverse the left subtree until reaching the leftmost node
        while root.left:
            root = root.left
        
        # Return the value of the leftmost node
        return root.data
