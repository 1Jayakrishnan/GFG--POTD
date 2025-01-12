class Solution:
    def maxWater(self, arr):
        if not arr or len(arr) < 3:
            return 0  # No water can be trapped if there are less than 3 blocks.
        
        left, right = 0, len(arr) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        
        while left < right:
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water_trapped += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water_trapped += right_max - arr[right]
                right -= 1
        
        return water_trapped
