class Solution:
    def longestCommonSubstr(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0

        return max_len
