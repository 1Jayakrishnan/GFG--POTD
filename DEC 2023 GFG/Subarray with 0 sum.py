class Solution:
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        # Create an empty set to store the running sum.
        sum_set = set()

        # Initialize the running sum.
        curr_sum = 0

        # Iterate through the array elements.
        for i in range(n):
            # Add the current element to the running sum.
            curr_sum += arr[i]

            # If the running sum is 0 or has been seen before, return True.
            if curr_sum == 0 or curr_sum in sum_set:
                return True

            # Add the current running sum to the set.
            sum_set.add(curr_sum)

        # If no subarray with 0 sum is found, return False.
        return False
