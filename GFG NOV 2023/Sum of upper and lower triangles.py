class Solution:
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        upper_sum = 0
        lower_sum = 0

        # Iterate through the matrix
        for i in range(n):
            for j in range(n):
                # Elements in the upper triangle (including the diagonal)
                if i <= j:
                    upper_sum += matrix[i][j]

                # Elements in the lower triangle (including the diagonal)
                if i >= j:
                    lower_sum += matrix[i][j]

        # Return the sum of upper and lower triangles
        return (upper_sum, lower_sum)
