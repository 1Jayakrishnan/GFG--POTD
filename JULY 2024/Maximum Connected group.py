from typing import List, Tuple

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        def dfs(x: int, y: int, comp_id: int) -> int:
            stack = [(x, y)]
            visited.add((x, y))
            component_map[(x, y)] = comp_id
            count = 0
            while stack:
                cx, cy = stack.pop()
                count += 1
                for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        component_map[(nx, ny)] = comp_id
                        stack.append((nx, ny))
            return count

        visited = set()
        component_size = {}
        component_map = {}
        component_id = 0

        # Step 1: Identify and count all connected components of 1s
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    size = dfs(i, j, component_id)
                    component_size[component_id] = size
                    component_id += 1

        max_size = max(component_size.values(), default=0)

        # Step 2: Evaluate changing each 0 to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_components = set()
                    new_size = 1  # We are changing grid[i][j] from 0 to 1
                    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            comp_id = component_map[(ni, nj)]
                            if comp_id not in seen_components:
                                seen_components.add(comp_id)
                                new_size += component_size[comp_id]
                    max_size = max(max_size, new_size)

        return max_size

