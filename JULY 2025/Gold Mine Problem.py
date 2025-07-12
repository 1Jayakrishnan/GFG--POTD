class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)      # rows
        m = len(mat[0])   # columns

        for col in range(m-2, -1, -1):  # from second last column to first
            for row in range(n):
                # Possible moves
                right = mat[row][col+1] if col+1 < m else 0
                right_up = mat[row-1][col+1] if row > 0 and col+1 < m else 0
                right_down = mat[row+1][col+1] if row < n-1 and col+1 < m else 0

                mat[row][col] += max(right, right_up, right_down)

        # Max gold will be max value in first column
        return max(mat[row][0] for row in range(n))
