class Solution:
    def noOfWays(self, m, n, x):
        dp = [0] * (x + 1)
        dp[0] = 1
        
        for dice in range(1, n + 1):
            next_dp = [0] * (x + 1)
            for target in range(1, x + 1):
                for face in range(1, m + 1):
                    if target - face >= 0:
                        next_dp[target] += dp[target - face]
            dp = next_dp
        
        return dp[x]
