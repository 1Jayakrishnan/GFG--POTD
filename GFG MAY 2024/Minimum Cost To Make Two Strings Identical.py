class Solution:
	def findMinCost(self, x, y, costX, costY):
		# code here
		m, n = len(x), len(y)
        
        # Initialize the dp array
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        # Base cases
        for i in range(1, m+1):
            dp[i][0] = i * costX
        for j in range(1, n+1):
            dp[0][j] = j * costY
        
        # Fill the dp array
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + costX, dp[i][j-1] + costY)
        
        return dp[m][n]
