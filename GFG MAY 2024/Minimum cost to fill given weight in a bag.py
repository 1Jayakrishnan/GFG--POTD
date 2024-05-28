from typing import List

class Solution:
    def minimumCost(self, n: int, w: int, cost: List[int]) -> int:
        # Initialize the dp array with a large value
        dp = [float('inf')] * (w + 1)
        
        # Cost to buy 0 kg of oranges is 0
        dp[0] = 0
        
        # Fill the dp array
        for i in range(1, n + 1):
            if cost[i - 1] != -1:  # If the packet of i kg is available
                for j in range(i, w + 1):
                    dp[j] = min(dp[j], dp[j - i] + cost[i - 1])
        
        # If dp[w] is still infinity, it's not possible to buy exactly w kg
        return dp[w] if dp[w] != float('inf') else -1
