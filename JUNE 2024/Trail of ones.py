class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        MOD = int(1e9+7)
        
        if n == 0:
            return 0
        
        # Initialize the dp arrays
        dp = [[0, 0] for _ in range(n+1)]
        
        # Base cases
        dp[1][0] = 1
        dp[1][1] = 1
        
        # Fill dp arrays
        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
            dp[i][1] = dp[i-1][0] % MOD
        
        # Total valid strings of length n
        total_valid_n = (dp[n][0] + dp[n][1]) % MOD
        
        # Total number of binary strings of length n
        total_all_n = pow(2, n, MOD)
        
        # Number of binary strings of length n with consecutive 1's
        result = (total_all_n - total_valid_n + MOD) % MOD
        
        return result
