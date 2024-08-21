from collections import defaultdict, deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Initialize the distance array
        dist = [float('inf')] * n
        dist[src] = 0
        
        # Step 3: BFS from the source node
        queue = deque([src])
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if dist[neighbor] == float('inf'):  # If the neighbor has not been visited
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        
        # Step 4: Replace unreachable nodes' distances with -1
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist
