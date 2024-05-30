class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        MOD = int(1e9 + 7)
        n = len(s1)
        m = len(s2)
        
        # Create a DP table with (n+1) x (m+1) dimensions
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base cases
        for i in range(n + 1):
            dp[i][0] = 1  # There's one way to match an empty s2

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    dp[i][j] = dp[i - 1][j] % MOD

        return dp[n][m]
