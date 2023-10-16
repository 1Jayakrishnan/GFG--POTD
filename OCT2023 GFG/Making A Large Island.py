from typing import List

class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        
        # Code here
        n = len(grid)
        maxIslandSize = 0

        def dfs(i, j, color):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = color
                return 1 + dfs(i - 1, j, color) + dfs(i + 1, j, color) + dfs(i, j - 1, color) + dfs(i, j + 1, color)
            return 0

        color = 2  # Starting color for marking islands

        # Step 1: Find and mark all islands, and store their sizes in a dictionary
        island_sizes = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[color] = dfs(i, j, color)
                    maxIslandSize = max(maxIslandSize, island_sizes[color])
                    color += 1

        # Step 2: Try changing '0' to '1' and check its effect on island size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < n and 0 <= y < n:
                            neighbors.add(grid[x][y])
                    total_size = 1  # The size if we change this '0' to '1'
                    for neighbor_color in neighbors:
                        total_size += island_sizes.get(neighbor_color, 0)
                    maxIslandSize = max(maxIslandSize, total_size)

        return maxIslandSize
