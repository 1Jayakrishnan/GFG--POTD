class Solution:
	def minPoints(self, m, n, points):
		# code here
		dp = [[0] * n for _ in range(m)]
        
        # Start from the bottom-right cell and work backwards.
        dp[m - 1][n - 1] = max(1, 1 - points[m - 1][n - 1])
        
        # Fill the last column with minimum points required to reach each cell.
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - points[i][n - 1])
        
        # Fill the last row with minimum points required to reach each cell.
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - points[m - 1][j])
        
        # Fill the rest of the table by considering the minimum points required to reach each cell.
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_points_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_points_on_exit - points[i][j])
        
        # The minimum points required to reach the starting cell (0, 0).
        return dp[0][0]
