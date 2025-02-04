class Solution:
    def diameter(self, root):
        # Your code here
        max_diameter = 0
        
        # Helper function to compute the height of the tree
        # while updating the diameter.
        def dfs(node):
            nonlocal max_diameter
            # Base case: If the node is None, height is -1.
            if not node:
                return -1
            
            # Recursively get the height of left and right subtrees.
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # The number of edges in the longest path that passes through the current node.
            current_diameter = left_height + right_height + 2
            
            # Update the global maximum diameter.
            max_diameter = max(max_diameter, current_diameter)
            
            # Return the height of the current node.
            return max(left_height, right_height) + 1
        
        dfs(root)
        return max_diameter
