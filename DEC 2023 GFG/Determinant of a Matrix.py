class Solution:
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        # code here 
        if n == 1:
            return matrix[0][0]

        # Initialize determinant value.
        det = 0

        # Iterate over each element of the first row.
        for i in range(n):
            # Calculate the cofactor matrix.
            cofactor = self.getCofactor(matrix, 0, i, n)
            
            # Add the determinant of this cofactor to the overall determinant.
            det += matrix[0][i] * ((-1) ** i) * self.determinantOfMatrix(cofactor, n - 1)

        return det

    # Helper function to get the cofactor matrix excluding the specified row and column.
    def getCofactor(self, matrix, row, col, n):
        return [[matrix[i][j] for j in range(n) if j != col] for i in range(n) if i != row]
