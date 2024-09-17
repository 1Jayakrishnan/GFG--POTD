class Solution:
    def getMinDiff(self, arr, k):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)
        
        # Initialize the answer as the difference between max and min height
        ans = arr[n-1] - arr[0]
        
        # Step 2: Traverse through the array and calculate the new min and max values
        for i in range(1, n):
            if arr[i] >= k:  # We can't decrease a value below zero, so skip those
                max_height = max(arr[i-1] + k, arr[n-1] - k)  # New max height
                min_height = min(arr[0] + k, arr[i] - k)  # New min height
                
                # Update the minimum difference
                ans = min(ans, max_height - min_height)
        
        return ans
