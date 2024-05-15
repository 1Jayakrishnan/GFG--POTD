from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        # Helper function for DFS traversal
        def dfs(email, graph, visited, emails):
            visited.add(email)
            emails.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, graph, visited, emails)
        
        # Build the graph
        graph = defaultdict(list)
        name_map = {}  # Maps email to name
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].append(account[1])
                graph[account[1]].append(email)
                name_map[email] = name
        
        # Perform DFS traversal to find connected components (accounts)
        merged_accounts = []
        visited = set()
        for email in graph:
            if email not in visited:
                emails = []
                dfs(email, graph, visited, emails)
                merged_accounts.append([name_map[email]] + sorted(emails))
        
        return merged_accounts
