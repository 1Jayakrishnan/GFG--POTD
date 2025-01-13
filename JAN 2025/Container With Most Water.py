class Solution:
    def maxWater(self, arr):
        if len(arr) < 2:
            return 0  # No container can be formed with less than 2 lines.
        
        left, right = 0, len(arr) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area with current left and right pointers
            height = min(arr[left], arr[right])
            width = right - left
            current_area = height * width
            
            # Update max_area if the current area is greater
            max_area = max(max_area, current_area)
            
            # Move the pointer of the smaller height
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
