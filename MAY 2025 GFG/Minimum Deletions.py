class Solution:
    def minDeletions(self, s):
        n = len(s)
        rev_s = s[::-1]
        
        # DP table: dp[i][j] = length of LCS of s[0..i-1] and rev_s[0..j-1]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prev = dp[:]
            for j in range(1, n + 1):
                if s[i - 1] == rev_s[j - 1]:
                    dp[j] = prev[j - 1] + 1
                else:
                    dp[j] = max(dp[j - 1], prev[j])
        
        lps = dp[n]
        return n - lps
