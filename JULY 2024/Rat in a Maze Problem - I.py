from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # Helper function for DFS traversal
        def dfs(x, y, path):
            # If destination is reached, add path to result
            if x == n - 1 and y == n - 1:
                result.append(path)
                return
            
            # Mark the current cell as visited
            m[x][y] = 0
            
            # Explore all possible directions
            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and m[nx][ny] == 1:
                    dfs(nx, ny, path + direction)
            
            # Unmark the current cell for other paths
            m[x][y] = 1

        if not m or m[0][0] == 0:
            return []
        
        n = len(m)
        result = []
        directions = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}
        
        # Start DFS from the top-left corner
        dfs(0, 0, '')
        
        return result
