class Solution:
    def getMinDiff(self,k, arr):
        # code here
        if len(arr) <= 1:
            return 0

        # Sort the array
        arr.sort()

        # Initial difference
        n = len(arr)
        initial_diff = arr[-1] - arr[0]

        # Minimum difference initialized to the initial difference
        min_diff = initial_diff

        # Iterate through the array
        for i in range(n - 1):
            # Current and next heights
            current = arr[i]
            next_height = arr[i + 1]

            # Calculate potential new max and min
            new_min = min(arr[0] + k, next_height - k)
            new_max = max(arr[-1] - k, current + k)

            # Update the minimum difference
            min_diff = min(min_diff, new_max - new_min)

        return min_diff
