class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        
        row_sum = [0] * n
        col_sum = [0] * n
        
        total_sum = 0
        
        for i in range(n):
            for j in range(n):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]
                total_sum += mat[i][j]
        
        # Target is the max of all row and column sums
        max_sum = max(max(row_sum), max(col_sum))
        
        # Total elements to become equal to max_sum per row/col
        return max_sum * n - total_sum
