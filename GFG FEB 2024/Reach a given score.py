class Solution:
    def count(self, n: int) -> int:
        # Create a list to store the number of combinations for each score
        dp = [0] * (n + 1)
        dp[0] = 1  # There is one way to get a score of 0 (by not making any move)

        # Iterate through possible scores
        for score in [3, 5, 10]:
            for i in range(score, n + 1):
                dp[i] += dp[i - score]

        return dp[n]
