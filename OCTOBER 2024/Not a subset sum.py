class Solution:
    def findSmallest(self, arr):
        # Initialize the smallest number that cannot be represented
        smallest_missing_sum = 1
        
        # Iterate over the sorted array
        for num in arr:
            # If current number is greater than the current smallest_missing_sum
            # we cannot form smallest_missing_sum anymore
            if num > smallest_missing_sum:
                break
            # Otherwise, add num to smallest_missing_sum
            smallest_missing_sum += num
        
        # Return the smallest number that cannot be represented
        return smallest_missing_sum
