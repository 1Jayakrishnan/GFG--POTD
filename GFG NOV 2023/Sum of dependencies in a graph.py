class Solution:
    def sumOfDependencies(self, adj, V):
        # Initialize sum to 0
        sum_of_dependencies = 0

        # Iterate through each node in the graph
        for i in range(V):
            # Increment sum by the size of the adjacency list for the current node
            sum_of_dependencies += len(adj[i])

        return sum_of_dependencies
