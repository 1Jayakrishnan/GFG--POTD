class Solution:
    def minDist(self, arr, n, x, y):
        last_x_index = -1
        last_y_index = -1
        min_distance = float('inf')

        # Iterate through the array
        for i in range(n):
            if arr[i] == x:
                if last_y_index != -1:
                    # If y has been seen before, calculate the distance
                    min_distance = min(min_distance, i - last_y_index)
                last_x_index = i
            elif arr[i] == y:
                if last_x_index != -1:
                    # If x has been seen before, calculate the distance
                    min_distance = min(min_distance, i - last_x_index)
                last_y_index = i

        # Check if either x or y was not found in the array
        if last_x_index == -1 or last_y_index == -1:
            return -1

        return min_distance
