class Solution:
    def matSearch(self, mat, x):
        # Get the dimensions of the matrix
        n = len(mat)       # Number of rows
        m = len(mat[0])    # Number of columns
        
        # Start from the top-right corner
        row = 0
        col = m - 1
        
        # Perform the search
        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                col -= 1  # Move left if the element is larger
            else:
                row += 1  # Move down if the element is smaller
        
        return False
