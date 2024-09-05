class Solution:
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        # code here
        total_sum = n * (n + 1) // 2
        # Calculate the sum of the array elements
        array_sum = sum(arr)
        # The missing number is the difference between the total sum and the array sum
        return total_sum - array_sum
        
