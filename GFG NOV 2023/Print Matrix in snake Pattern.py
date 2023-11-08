class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
        result = []
        rows = len(matrix)
        if rows == 0:
            return result  # Handle empty matrix

        cols = len(matrix[0])

        for i in range(rows):
            if i % 2 == 0:
                # Even row, left to right
                for j in range(cols):
                    result.append(matrix[i][j])
            else:
                # Odd row, right to left
                for j in range(cols - 1, -1, -1):
                    result.append(matrix[i][j])

        return result
