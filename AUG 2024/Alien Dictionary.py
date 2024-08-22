from collections import defaultdict, deque
from typing import List
class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Step 1: Create the graph
        graph = defaultdict(list)
        in_degree = {chr(i + ord('a')): 0 for i in range(k)}
        
        # Step 2: Build the graph by comparing adjacent words
        for i in range(n - 1):
            word1 = dict[i]
            word2 = dict[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Find the first differing character
            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break
        
        # Step 3: Topological Sort (BFS - Kahn's Algorithm)
        queue = deque([ch for ch in in_degree if in_degree[ch] == 0])
        order = []
        
        while queue:
            ch = queue.popleft()
            order.append(ch)
            
            for neighbor in graph[ch]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If order contains all characters, return it as a string
        if len(order) == k:
            return ''.join(order)
        else:
            return ""  # In case of a cycle or invalid input
