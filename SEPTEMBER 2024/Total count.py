class Solution:
    def totalCount(self, k, arr):
        # code here
        total_parts = 0
        
        # Traverse through each element in the array
        for num in arr:
            # Calculate the number of parts for each element
            parts = (num + k - 1) // k  # This is the ceiling of num / k
            total_parts += parts
        
        # Return the total number of parts
        return total_parts
