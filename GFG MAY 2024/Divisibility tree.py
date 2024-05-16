from collections import defaultdict
from typing import List


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize the count of nodes in each subtree
        subtree_count = [0] * (n + 1)
        
        # Helper function for DFS traversal to count nodes in each subtree
        def dfs(node, parent):
            count = 1  # Count the current node
            for neighbor in graph[node]:
                if neighbor != parent:
                    count += dfs(neighbor, node)
            subtree_count[node] = count
            return count
        
        # Perform DFS traversal starting from the root node (1)
        dfs(1, 0)
        
        # Count the number of edges that need to be removed
        edge_remove_count = 0
        for node in range(2, n + 1):
            if subtree_count[node] % 2 == 0:
                edge_remove_count += 1
        
        return edge_remove_count
        
