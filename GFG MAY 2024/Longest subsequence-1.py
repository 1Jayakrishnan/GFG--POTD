from typing import List

class Solution:
    def longestSubseq(self, n: int, a: List[int]) -> int:
        # Initialize dp array with 1 as each element is a subsequence of length 1
        dp = [1] * n
        
        # Fill the dp array
        for i in range(1, n):
            for j in range(i):
                if abs(a[i] - a[j]) == 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Return the maximum value from dp array
        return max(dp)
