class Solution:
    def sumOfLongRootToLeafPath(self, root):
        # Helper function to perform DFS
        def dfs(node, curr_sum, curr_len):
            if not node:
                return (curr_len, curr_sum)
            
            # Recur for left and right subtree
            left_len, left_sum = dfs(node.left, curr_sum + node.data, curr_len + 1)
            right_len, right_sum = dfs(node.right, curr_sum + node.data, curr_len + 1)
            
            # Choose the longer path; if equal, choose the one with higher sum
            if left_len > right_len:
                return (left_len, left_sum)
            elif right_len > left_len:
                return (right_len, right_sum)
            else:
                return (left_len, max(left_sum, right_sum))
        
        # Call DFS with initial values
        return dfs(root, 0, 0)[1]
