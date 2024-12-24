
class Solution:
    # Function to search a given number in a strictly sorted matrix.
    def searchMatrix(self, mat, x):
        if not mat or not mat[0]:
            return False

        rows = len(mat)
        cols = len(mat[0])
        
        # Treat the 2D matrix as a 1D array
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index back to 2D indices
            row, col = divmod(mid, cols)
            mid_value = mat[row][col]
            
            if mid_value == x:
                return True
            elif mid_value < x:
                left = mid + 1
            else:
                right = mid - 1

        return False
