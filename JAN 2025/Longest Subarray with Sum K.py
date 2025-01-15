class Solution:
    def longestSubarray(self, arr, k):
        # Initialize variables
        prefix_sum = 0
        max_length = 0
        prefix_map = {}
        
        # Traverse the array
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            # Case 1: Subarray starts from the beginning
            if prefix_sum == k:
                max_length = i + 1
            
            # Case 2: Check if prefix_sum - k exists in the map
            if (prefix_sum - k) in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum - k])
            
            # Store the prefix_sum in the map if not already present
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return max_length
