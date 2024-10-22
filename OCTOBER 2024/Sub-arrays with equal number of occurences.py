class Solution:
    def sameOccurrence(self, arr, x, y):
        # Initialize variables
        diff_map = {0: 1}  # Store the count of differences, 0 means equal x and y
        count_x = 0
        count_y = 0
        diff_count = 0
        result = 0
        
        for num in arr:
            # Update count_x and count_y
            if num == x:
                count_x += 1
            if num == y:
                count_y += 1
            
            # Calculate the difference
            diff_count = count_x - count_y
            
            # If this difference has been seen before, we have valid subarrays
            if diff_count in diff_map:
                result += diff_map[diff_count]
            
            # Update the map with the current difference count
            if diff_count in diff_map:
                diff_map[diff_count] += 1
            else:
                diff_map[diff_count] = 1
        
        return result
