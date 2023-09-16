class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        # code here
        MOD = 1000000007
        
        # Create an array to store the number of ways to reach each step.
        dp = [0] * (n + 1)
        
        # There is one way to reach the 0th step (base case).
        dp[0] = 1
        
        for i in range(1, n + 1):
            # Calculate the number of ways to reach the current step
            # by taking 1, 2, or 3 steps from the previous steps.
            for j in range(1, 4):
                if i - j >= 0:
                    dp[i] = (dp[i] + dp[i - j]) % MOD
        
        # Return the number of ways to reach the Nth step modulo 1000000007.
        return dp[n]
