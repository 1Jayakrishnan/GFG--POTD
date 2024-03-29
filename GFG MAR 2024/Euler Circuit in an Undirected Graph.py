class Solution:
	def isEularCircuitExist(self, v, adj):
		#Code here
		degrees = [len(neighbors) for neighbors in adj]
        
        # Check if every vertex has an even degree
        for degree in degrees:
            if degree % 2 != 0:
                return 0
        
        # If all vertices have an even degree, return 1
        return 1

    
    def isConnected(self, v, adj):
        # Depth-first search to check connectivity
        visited = [False] * v
        self.DFS(adj, 0, visited)
        
        # Check if all vertices are visited
        return all(visited)
    
    def DFS(self, adj, vertex, visited):
        visited[vertex] = True
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                self.DFS(adj, neighbor, visited)
