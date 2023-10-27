class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here 
        n = len(S)

        # Create a table to store the length of the LPS
        dp = [[0] * n for _ in range(n)]

        # Initialize the diagonal elements to 1 (a single character is always a palindrome)
        for i in range(n):
            dp[i][i] = 1

        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if S[i] == S[j] and cl == 2:
                    dp[i][j] = 2
                elif S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the LPS of the entire string
        lps_length = dp[0][n - 1]

        # Calculate the minimum number of deletions required
        min_deletions = n - lps_length

        return min_deletions
