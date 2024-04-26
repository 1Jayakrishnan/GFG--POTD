class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize current position and direction
        row, col = 0, 0
        direction = 0  # Start with moving right
        
        # Simulate movement through the matrix
        while True:
            # Check if current cell contains 1
            if matrix[row][col] == 1:
                matrix[row][col] = 0  # Change 1 to 0
                direction = (direction + 1) % 4  # Change direction to the right
            
            # Move to the next cell based on the current direction
            next_row = row + directions[direction][0]
            next_col = col + directions[direction][1]

            # If the next cell is out of bounds, return the current position as exit point
            if not (0 <= next_row < n and 0 <= next_col < m):
                return (row, col)
            
            # Update the current position
            row, col = next_row, next_col
