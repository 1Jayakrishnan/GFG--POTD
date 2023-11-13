class Solution:
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
         #code here
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table using bottom-up approach.
        for i in range(m + 1):
            for j in range(n + 1):
                # If one of the strings is empty, the length of the supersequence is the length of the other string.
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                # If the characters match, reduce the problem to the shorter strings.
                elif X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # If characters don't match, take the minimum length of supersequence without one character.
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        # The length of the shortest common supersequence is given by the last cell of the DP table.
        return dp[m][n]
