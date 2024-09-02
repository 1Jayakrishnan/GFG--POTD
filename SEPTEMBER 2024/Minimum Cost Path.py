from heapq import heappush, heappop

class Solution:
    
    def minimumCostPath(self, grid):
        n = len(grid)
        
        # Initialize min_cost array to store the minimum cost to reach each cell
        min_cost = [[float('inf')] * n for _ in range(n)]
        min_cost[0][0] = grid[0][0]
        
        # Min-heap to store (cost, x, y)
        heap = [(grid[0][0], 0, 0)]
        
        # Directions for moving up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            current_cost, x, y = heappop(heap)
            
            # If we reached the bottom-right corner
            if x == n - 1 and y == n - 1:
                return current_cost
            
            # Explore all possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = current_cost + grid[nx][ny]
                    
                    # If new path is cheaper, update and push to heap
                    if new_cost < min_cost[nx][ny]:
                        min_cost[nx][ny] = new_cost
                        heappush(heap, (new_cost, nx, ny))
        
        return min_cost[n-1][n-1]
