from collections import defaultdict, deque

class Solution:
    def findOrder(self, n, m, prerequisites):
        # Create adjacency list representation of the graph
        graph = defaultdict(list)
        in_degree = [0] * n

        for pair in prerequisites:
            course, prerequisite = pair
            graph[prerequisite].append(course)
            in_degree[course] += 1

        # Initialize a queue for topological sort
        queue = deque()

        # Add courses with in-degree 0 to the queue
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize the result order
        result = []

        # Perform topological sort
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If not all courses are included in the result, return empty array
        if len(result) != n:
            return []

        return result
