class Solution:
    def aggressiveCows(self, stalls, k):
        # Function to check if cows can be placed with minimum distance 'mid'
        def canPlaceCows(stalls, k, mid):
            count_cows = 1  # Place the first cow
            last_position = stalls[0]  # Place at the first stall
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= mid:  # Check if distance >= mid
                    count_cows += 1
                    last_position = stalls[i]  # Update the position of the last cow
                    if count_cows == k:  # If all cows are placed, return True
                        return True
            return False

        # Sort the stalls to place cows in increasing order of positions
        stalls.sort()
        
        # Initialize binary search range
        low = 1  # Minimum possible distance
        high = stalls[-1] - stalls[0]  # Maximum possible distance
        result = 0
        
        while low <= high:
            mid = (low + high) // 2  # Candidate minimum distance
            if canPlaceCows(stalls, k, mid):  # Check feasibility
                result = mid  # Update result if cows can be placed
                low = mid + 1  # Try for a larger minimum distance
            else:
                high = mid - 1  # Reduce the distance
        
        return result
