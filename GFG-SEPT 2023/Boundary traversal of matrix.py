class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        boundary = []

        if n == 1:
            # If there is only one row, add the entire row to the boundary.
            boundary.extend(matrix[0])
        elif m == 1:
            # If there is only one column, add the entire column to the boundary.
            for i in range(n):
                boundary.append(matrix[i][0])
        else:
            for i in range(m):
                boundary.append(matrix[0][i])  # Traverse the first row

            for i in range(1, n):
                boundary.append(matrix[i][m - 1])  # Traverse the last column

            if n > 1:
                for i in range(m - 2, -1, -1):
                    boundary.append(matrix[n - 1][i])  # Traverse the last row

            if m > 1:
                for i in range(n - 2, 0, -1):
                    boundary.append(matrix[i][0])  # Traverse the first column

        return boundary
