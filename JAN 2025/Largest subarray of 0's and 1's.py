class Solution:
    def maxLen(self, arr):
        # Replace 0s with -1s
        arr = [-1 if num == 0 else 1 for num in arr]
        
        # Initialize variables
        prefix_sum = 0
        max_length = 0
        hash_map = {}
        
        # Traverse the array
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            # Case 1: If prefix_sum is 0, the subarray from 0 to i is balanced
            if prefix_sum == 0:
                max_length = i + 1
            
            # Case 2: If prefix_sum has been seen before
            if prefix_sum in hash_map:
                max_length = max(max_length, i - hash_map[prefix_sum])
            else:
                # Store the first occurrence of the prefix_sum
                hash_map[prefix_sum] = i
        
        return max_length
