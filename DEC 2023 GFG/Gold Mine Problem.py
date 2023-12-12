class Solution:
    def maxGold(self, n, m, M):
        # code here
        # Create a 2D table to store the maximum gold values
        dp = [[0] * m for _ in range(n)]

        # Copy the values from the first column of the mine to the dp table
        for i in range(n):
            dp[i][0] = M[i][0]

        # Iterate through the columns starting from the second column
        for j in range(1, m):
            for i in range(n):
                # Consider the three possible moves: diagonal up, right, diagonal down
                moves = [dp[i][j - 1]]
                if i > 0:
                    moves.append(dp[i - 1][j - 1])
                if i < n - 1:
                    moves.append(dp[i + 1][j - 1])

                # Update the maximum gold value for the current cell
                dp[i][j] = M[i][j] + max(moves)

        # Find the maximum value in the last column
        max_gold = max(dp[i][m - 1] for i in range(n))

        return max_gold
