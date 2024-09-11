from collections import defaultdict, deque

class Solution:
    def isCircle(self, arr):
        # Helper function to perform DFS
        def dfs(v, adj, visited):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, adj, visited)
        
        # Step 1: Create an adjacency list
        n = len(arr)
        adj = defaultdict(list)  # Adjacency list for graph representation
        rev_adj = defaultdict(list)  # Reverse adjacency list for reverse DFS
        in_degree = defaultdict(int)  # To store in-degree for each character
        out_degree = defaultdict(int)  # To store out-degree for each character
        
        for word in arr:
            first_char = word[0]
            last_char = word[-1]
            adj[first_char].append(last_char)
            rev_adj[last_char].append(first_char)
            out_degree[first_char] += 1
            in_degree[last_char] += 1
        
        # Step 2: Check if in-degree equals out-degree for every character
        for char in out_degree:
            if out_degree[char] != in_degree[char]:
                return 0  # Not possible to form a circle
        
        # Step 3: Perform DFS to check if all characters form a single connected component
        # Find the first character that has an outgoing edge
        start_char = arr[0][0]
        
        # DFS on the original graph
        visited = defaultdict(bool)
        dfs(start_char, adj, visited)
        
        # Check if all nodes with outgoing edges were visited
        for char in out_degree:
            if out_degree[char] > 0 and not visited[char]:
                return 0  # Not all nodes are connected
        
        # DFS on the reverse graph
        visited = defaultdict(bool)
        dfs(start_char, rev_adj, visited)
        
        # Check if all nodes with incoming edges were visited
        for char in in_degree:
            if in_degree[char] > 0 and not visited[char]:
                return 0  # Not all nodes are connected in reverse
        
        # If both DFS traversals pass, the strings can form a circle
        return 1
