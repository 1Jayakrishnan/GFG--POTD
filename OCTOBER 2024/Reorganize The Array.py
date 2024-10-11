class Solution:
    def rearrange(self, arr):
        n = len(arr)
        new_arr = [-1] * n  # Initialize result array with -1
        
        # Directly place elements in their correct position if possible
        for i in range(n):
            if 0 <= arr[i] < n:
                new_arr[arr[i]] = arr[i]
                
        return new_arr
