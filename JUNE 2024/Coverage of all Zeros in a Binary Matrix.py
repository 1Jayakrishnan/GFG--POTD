class Solution:
	def findCoverage(self, matrix):
		# Code here
		# Initialize the total coverage
        total_coverage = 0
        
        # Get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Function to get the value of a cell, return 0 if out of bounds
        def get_value(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return matrix[r][c]
            return 0
        
        # Iterate through each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Sum the values of the surrounding cells
                    coverage = (get_value(i-1, j) +  # up
                                get_value(i+1, j) +  # down
                                get_value(i, j-1) +  # left
                                get_value(i, j+1))   # right
                    # Add the coverage of the current zero to the total coverage
                    total_coverage += coverage
        
        return total_coverage
