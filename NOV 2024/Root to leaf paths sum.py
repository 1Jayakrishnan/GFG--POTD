class Solution:
    def treePathSum(self,root):
        # Code here
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Calculate the current path sum
            current_sum = current_sum * 10 + node.data
            
            # If it's a leaf node, return the current path sum
            if not node.left and not node.right:
                return current_sum
            
            # Recursively calculate the sum for left and right subtrees
            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)
            
            # Return the total sum from both subtrees
            return left_sum + right_sum
        
        # Initialize the DFS traversal from root with an initial sum of 0
        return dfs(root, 0)
