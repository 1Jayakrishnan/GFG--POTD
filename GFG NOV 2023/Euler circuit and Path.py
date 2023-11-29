from collections import defaultdict

class Solution:
    def isEulerCircuitExist(self, V, adj):
        # Count the degree of each vertex
        degrees = [0] * V
        for u in range(V):
            degrees[u] = len(adj[u])

        # Count vertices with odd degree
        odd_degree_count = sum(1 for degree in degrees if degree % 2 != 0)

        # Check for Eulerian circuit, Eulerian path, or neither
        if odd_degree_count == 0:
            return 2  # Eulerian Circuit
        elif odd_degree_count == 2:
            return 1  # Eulerian Path
        else:
            return 0  # Neither
