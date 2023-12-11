class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        # Initialize variables to store the current sum and maximum sum
        current_sum = max_sum = sum(Arr[:K])

        # Iterate through the array to find the maximum sum of subarrays of size K
        for i in range(K, N):
            # Subtract the element leaving the window and add the new element entering the window
            current_sum = current_sum - Arr[i - K] + Arr[i]

            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum
