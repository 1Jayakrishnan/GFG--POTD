
class Solution:
    
    def DFS(self, v, visited, adj):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited, adj)
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here
		visited = [False] * V
        last_v = 0  # Initialize the last visited vertex

        # Perform DFS from all vertices to find the last visited vertex
        for i in range(V):
            if not visited[i]:
                self.DFS(i, visited, adj)
                last_v = i

        # Check if the last visited vertex can reach all other vertices
        visited = [False] * V
        self.DFS(last_v, visited, adj)

        # If the last visited vertex can reach all other vertices, it's a mother vertex
        if all(visited):
            return last_v
        else:
            return -1  # No mother vertex found
