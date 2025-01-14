class Solution:
    def findEquilibrium(self, arr):
        # Step 1: Calculate total sum of the array
        total_sum = sum(arr)
        left_sum = 0
        
        # Step 2: Traverse the array and check for equilibrium
        for i in range(len(arr)):
            # Right sum = total sum - left sum - current element
            right_sum = total_sum - left_sum - arr[i]
            
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i  # Return 0-based index
            
            # Update left sum
            left_sum += arr[i]
        
        # If no equilibrium point found, return -1
        return -1
