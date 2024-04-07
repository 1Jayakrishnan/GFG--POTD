class Solution:
	def maxDotProduct(self, n, m, a, b):
		# dp[i][j] = max(dp[i-1][j-1] + a[i]*b[j], dp[i-1][j])
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(min(m, i+1)):
                dp[i+1][j+1] = max(dp[i][j] + a[i]*b[j], dp[i][j+1])
        
        return dp[n][m]
