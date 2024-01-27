class Solution:
    def matrixChainOrder(self, p, n):
        # Create a 2D array to store the minimum number of multiplications
        dp = [[float('inf')] * n for _ in range(n)]

        # Initialize the diagonal elements to zero
        for i in range(n):
            dp[i][i] = 0

        # s matrix is used to reconstruct the optimal solution
        s = [[0] * n for _ in range(n)]

        # Fill the dp array using bottom-up approach
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        s[i][j] = k

        # Reconstruct the optimal parenthesization
        return self.printOptimalParentheses(s, 1, n - 1)

    def printOptimalParentheses(self, s, i, j):
        if i == j:
            return chr(ord('A') + i - 1)

        left = self.printOptimalParentheses(s, i, s[i][j])
        right = self.printOptimalParentheses(s, s[i][j] + 1, j)

        return '(' + left + right + ')'
