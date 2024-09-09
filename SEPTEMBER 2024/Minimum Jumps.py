class Solution:
    def minJumps(self, arr):
        # If the array has only one element or the first element is 0, we cannot move
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] == 0:
            return -1
        
        # Initialize variables
        maxReach = arr[0]  # the farthest point we can reach
        steps = arr[0]     # steps we can take from the current position
        jumps = 1          # at least one jump needed to start moving
        
        # Loop through the array
        for i in range(1, n):
            # If we reach the end of the array
            if i == n - 1:
                return jumps
            
            # Update maxReach to the farthest point we can reach
            maxReach = max(maxReach, i + arr[i])
            
            # Use one step to move from i to i+1
            steps -= 1
            
            # If we have used all steps, we need to make a jump
            if steps == 0:
                jumps += 1
                # Check if the current index is beyond the maxReach
                if i >= maxReach:
                    return -1
                
                # Reinitialize steps to the remaining steps we can take from this position
                steps = maxReach - i
        
        return -1
