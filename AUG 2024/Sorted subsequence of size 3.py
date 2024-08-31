class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []

        # Initialize arrays
        smallest_left = [0] * n
        largest_right = [0] * n

        # Fill smallest_left
        smallest_left[0] = float('inf')  # No left element for the first element
        for i in range(1, n):
            smallest_left[i] = min(smallest_left[i - 1], arr[i - 1])

        # Fill largest_right
        largest_right[n - 1] = float('-inf')  # No right element for the last element
        for i in range(n - 2, -1, -1):
            largest_right[i] = max(largest_right[i + 1], arr[i + 1])

        # Find the triplet
        for i in range(n):
            if smallest_left[i] < arr[i] < largest_right[i]:
                return [smallest_left[i], arr[i], largest_right[i]]

        return []
