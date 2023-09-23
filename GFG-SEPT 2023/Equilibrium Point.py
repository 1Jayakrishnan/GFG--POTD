class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
         # Calculate the total sum of the array.
        total_sum = sum(A)
        
        # Initialize the prefix sum and suffix sum.
        prefix_sum = 0
        suffix_sum = total_sum
        
        for i in range(N):
            # Update the suffix sum by subtracting the current element.
            suffix_sum -= A[i]
            
            # Check if the prefix sum is equal to the suffix sum.
            if prefix_sum == suffix_sum:
                return i + 1  # Equilibrium point found at index i
            
            # Update the prefix sum by adding the current element.
            prefix_sum += A[i]
        
        # If no equilibrium point is found, return -1.
        return -1
