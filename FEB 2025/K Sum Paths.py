class Solution:
    def sumK(self,root,k):
        # code here
        def dfs(node, curr_sum, prefix):
            if node is None:
                return 0
            
            # Update current cumulative sum.
            curr_sum += node.data
            
            # Count how many times we've seen (curr_sum - k) as that many paths
            # end at this node with sum k.
            count = prefix.get(curr_sum - k, 0)
            
            # Update the prefix map for the current sum.
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            # Recurse into left and right subtrees.
            count += dfs(node.left, curr_sum, prefix)
            count += dfs(node.right, curr_sum, prefix)
            
            # Backtrack: remove the current sum from the map.
            prefix[curr_sum] -= 1
            
            return count
        
        # Initialize prefix dictionary with 0:1.
        prefix = {0: 1}
        return dfs(root, 0, prefix)
