class Solution:
    def pairWithMaxSum(self, arr):
        # If the array has fewer than two elements, return -1
        if len(arr) < 2:
            return -1
        
        # Initialize max_sum with the sum of the first pair
        max_sum = arr[0] + arr[1]
        
        # Traverse the array and find the maximum sum of consecutive pairs
        for i in range(1, len(arr) - 1):
            pair_sum = arr[i] + arr[i + 1]
            if pair_sum > max_sum:
                max_sum = pair_sum
        
        return max_sum
