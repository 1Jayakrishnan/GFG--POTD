class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        max_profit = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                max_profit += (arr[i] - arr[i-1])
        
        return max_profit
