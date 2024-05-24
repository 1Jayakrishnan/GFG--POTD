from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        MOD = 10**9 + 7
        total_sum = sum(arr)
        
        # If (total_sum + d) is odd, it's not possible to partition the array
        if (total_sum + d) % 2 != 0:
            return 0
        
        target_sum = (total_sum + d) // 2
        
        # If target_sum is negative, it's not possible to partition the array
        if target_sum < 0:
            return 0
        
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # There's one way to have a sum of 0: by picking no elements
        
        for num in arr:
            for j in range(target_sum, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[target_sum]
        
