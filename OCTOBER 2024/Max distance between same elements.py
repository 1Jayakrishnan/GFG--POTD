class Solution:
    def maxDistance(self, arr):
        # Dictionary to store the first occurrence of elements
        first_occurrence = {}
        max_dist = 0
        
        # Traverse the array
        for i in range(len(arr)):
            # If the element is seen for the first time, store its index
            if arr[i] not in first_occurrence:
                first_occurrence[arr[i]] = i
            else:
                # Calculate the distance from its first occurrence
                distance = i - first_occurrence[arr[i]]
                # Update the maximum distance
                max_dist = max(max_dist, distance)
        
        return max_dist
