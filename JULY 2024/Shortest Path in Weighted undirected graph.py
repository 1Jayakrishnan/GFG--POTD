from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Create adjacency list
        graph = {i: [] for i in range(1, n+1)}
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        # Dijkstra's algorithm
        min_heap = [(0, 1)]  # (distance, node)
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[1] = 0
        previous = {i: None for i in range(1, n+1)}
        
        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(min_heap, (distance, neighbor))
        
        # No path found
        if distances[n] == float('inf'):
            return [-1]
        
        # Reconstruct path
        path = []
        current_node = n
        while current_node is not None:
            path.append(current_node)
            current_node = previous[current_node]
        path.reverse()
        
        # Return the result with the total weight as the first element
        return [distances[n]] + path

        
