class Solution:
    def find(self, arr, n, x):
        
        # code here   # Initialize variables to store the first and last occurrence indices.
        first_occurrence = -1
        last_occurrence = -1
        
        # Binary search to find the first occurrence.
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                first_occurrence = mid
                right = mid - 1  # Continue searching in the left subarray.
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # Reset left and right pointers for the last occurrence search.
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                last_occurrence = mid
                left = mid + 1  # Continue searching in the right subarray.
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # Return the first and last occurrence indices.
        return [first_occurrence, last_occurrence]
        
