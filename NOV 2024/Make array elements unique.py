class Solution:
    def minIncrements(self, arr):
        # Sort the array
        arr.sort()
        
        # Initialize the number of increments
        increments = 0

        # Traverse the sorted array
        for i in range(1, len(arr)):
            # If the current element is less than or equal to the previous one
            if arr[i] <= arr[i - 1]:
                # Calculate needed increment to make it unique
                increment_needed = arr[i - 1] - arr[i] + 1
                arr[i] += increment_needed
                increments += increment_needed
        
        return increments
