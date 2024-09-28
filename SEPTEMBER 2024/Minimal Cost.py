class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        # Initialize a dp array to store the minimum cost to reach each stone
        dp = [float('inf')] * n
        dp[0] = 0  # No cost to start at the first stone
        
        # Fill the dp array
        for i in range(1, n):
            # Check all possible jumps from stone i-k to i-1
            for j in range(1, min(k, i) + 1):
                dp[i] = min(dp[i], dp[i - j] + abs(arr[i] - arr[i - j]))
        
        # Return the minimum cost to reach the last stone
        return dp[-1]
