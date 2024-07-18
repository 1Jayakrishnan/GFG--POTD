class Solution:
    def alternatingMaxLength(self, arr):
        if not arr:
            return 0

        # Initialize variables to track the lengths of increasing and decreasing subsequences
        inc = 1
        dec = 1

        # Iterate through the array
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1

        # The answer is the maximum of the two lengths
        return max(inc, dec)
