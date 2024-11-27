class Solution:
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)

        # Rearrange the array: Place numbers at their correct index
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

        # Check for the first missing positive number
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1

        # If all are in place, return n+1
        return n + 1
