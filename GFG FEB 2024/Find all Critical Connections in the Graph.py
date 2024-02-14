class Solution:
    def criticalConnections(self, v, adj):
        def dfs(node, parent, discovery, low, result, adj):
            nonlocal time
            discovery[node] = low[node] = time
            time += 1
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                if discovery[neighbor] == -1:  # If the neighbor is not visited
                    dfs(neighbor, node, discovery, low, result, adj)
                    low[node] = min(low[node], low[neighbor])
                    
                    if low[neighbor] > discovery[node]:
                        result.append(tuple(sorted([node, neighbor])))
                else:
                    low[node] = min(low[node], discovery[neighbor])

        discovery = [-1] * v
        low = [-1] * v
        result = []
        time = 0

        for i in range(v):
            if discovery[i] == -1:
                dfs(i, -1, discovery, low, result, adj)

        return sorted(result)
