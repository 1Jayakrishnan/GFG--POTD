from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        adjacency_list = [[] for _ in range(V)]

        # Iterate through the edges and add them to the adjacency list
        for edge in edges:
            u, v = edge
            # Since the graph is undirected, we add both u to v and v to u
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        return adjacency_list
