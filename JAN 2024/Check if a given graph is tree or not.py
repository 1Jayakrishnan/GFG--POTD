class Solution:
    def isTree(self, n, m, edges):
        # Code here
        adjacency_list = {i: [] for i in range(n)}
        for edge in edges:
            u, v = edge
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # Initialize visited set and parent array
        visited = set()
        parent = [-1] * n

        # DFS function
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    parent[neighbor] = node
                    if not dfs(neighbor, parent):
                        return False
                elif parent[node] != neighbor:
                    # There is a cycle
                    return False
            return True

        # Check for connectivity and cycles
        if not dfs(0, parent):
            return 0

        # Check if all nodes are visited
        return 1 if len(visited) == n else 0

