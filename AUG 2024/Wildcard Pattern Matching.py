class Solution:
    def wildCard(self, pattern, string):
        m = len(pattern)
        n = len(string)
        
        # DP table initialization
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Fill for patterns starting with '*'
        for i in range(1, m + 1):
            if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        
        # Fill the rest of the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return 1 if dp[m][n] else 0
