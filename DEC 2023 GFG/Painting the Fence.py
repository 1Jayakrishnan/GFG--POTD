class Solution:
    def countWays(self,n,k):
        #code here.
        if n == 0:
            return 0
        if n == 1:
            return k

        # Define the modulo constant
        MOD = 10**9 + 7

        # Initialize variables for the first two fences
        same_color = k  # Number of ways to paint the first two fences with the same color
        diff_color = k * (k - 1)  # Number of ways to paint the first two fences with different colors

        # Iterate through the remaining fences
        for i in range(3, n + 1):
            # Calculate the number of ways to paint the current fence with the same color
            same_color, diff_color = diff_color, (same_color + diff_color) * (k - 1) % MOD

        # The final result is the sum of the ways to paint the last two fences
        return (same_color + diff_color) % MOD
