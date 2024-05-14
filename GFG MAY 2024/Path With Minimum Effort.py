
from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        """
        This function calculates the minimum effort required to travel from the top-left cell to the bottom-right cell.
        
        Args:
        rows (int): The number of rows in the 2D array.
        columns (int): The number of columns in the 2D array.
        heights (List[List[int]]): A 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col).
        
        Returns:
        int: The minimum effort required to travel from the top-left cell to the bottom-right cell.
        """
        
        # Define the directions for moving up, down, left, and right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Create a priority queue to store the cells to be processed
        pq = [(0, 0, 0)]  # (effort, row, col)
        
        # Create a 2D array to store the minimum effort required to reach each cell
        efforts = [[float('inf')] * columns for _ in range(rows)]
        efforts[0][0] = 0
        
        while pq:
            effort, row, col = heapq.heappop(pq)
            
            # If the current effort is greater than the minimum effort required to reach this cell, skip it
            if effort > efforts[row][col]:
                continue
            
            # Process the neighbors of the current cell
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                # Check if the neighbor is within the bounds of the 2D array
                if 0 <= nr < rows and 0 <= nc < columns:
                    # Calculate the new effort required to reach the neighbor
                    new_effort = max(effort, abs(heights[nr][nc] - heights[row][col]))
                    
                    # If the new effort is less than the minimum effort required to reach the neighbor, update it
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
        
        # Return the minimum effort required to reach the bottom-right cell
        return efforts[rows - 1][columns - 1]
