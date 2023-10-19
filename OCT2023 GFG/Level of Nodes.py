from collections import deque
class Solution:
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        visited = [False] * V
        # Initialize a queue for BFS.
        queue = deque()
        
        # Mark the source node (0) as visited and enqueue it.
        visited[0] = True
        queue.append((0, 0))  # Tuple format: (node, level)
        
        while queue:
            node, level = queue.popleft()
            
            # If the current node is the target node X, return its level.
            if node == X:
                return level
            
            # Traverse all adjacent nodes of the current node.
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, level + 1))
        
        # If the target node X is not reachable, return -1.
        return -1
