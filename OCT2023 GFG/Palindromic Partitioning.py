class Solution:
    def palindromicPartition(self, string):
        # code here
        def is_palindrome(s):
            return s == s[::-1]

        n = len(string)
        
        # Initialize a 2D table to store the minimum cuts
        # dp[i][j] will be True if the string from index i to j is a palindrome
        dp = [[False] * n for _ in range(n)]

        # Initialize the cuts array to store the minimum cuts
        cuts = [0] * n

        for i in range(n):
            min_cuts = i  # Maximum cuts needed in the worst case

            for j in range(i, -1, -1):
                if string[i] == string[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if j == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, cuts[j - 1] + 1)

            cuts[i] = min_cuts

        return cuts[n - 1]
