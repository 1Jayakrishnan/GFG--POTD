class Solution:
    def maxSum(self, arr):
        n = len(arr)
        if n < 2:
            return 0  # no subarray of length at least 2
        
        maxScore = 0
        
        for i in range(n - 1):
            small = min(arr[i], arr[i+1])
            second_small = max(arr[i], arr[i+1])
            maxScore = max(maxScore, small + second_small)
        
        return maxScore
