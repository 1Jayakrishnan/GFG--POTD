class Solution:
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        max_steps = 0
        current_steps = 0
        
        # Traversing the array starting from the second element.
        for i in range(1, len(arr)):
            # If the current building is taller than the previous one.
            if arr[i] > arr[i-1]:
                current_steps += 1
                # Updating the maximum steps if needed.
                max_steps = max(max_steps, current_steps)
            else:
                # Reset the current steps if the sequence breaks.
                current_steps = 0
        
        # Return the maximum consecutive steps found.
        return max_steps
