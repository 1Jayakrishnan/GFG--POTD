class Solution:
    def sumClosest(self, arr, target):
        # Handle the edge case of less than 2 elements
        if len(arr) < 2:
            return []
        
        # Sort the array
        arr.sort()
        left, right = 0, len(arr) - 1
        closest_sum = float('inf')  # To track the closest sum
        result = []
        max_abs_diff = 0  # To track the maximum absolute difference

        while left < right:
            a, b = arr[left], arr[right]
            current_sum = a + b

            # Update if the current sum is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target) or \
               (abs(current_sum - target) == abs(closest_sum - target) and (b - a) > max_abs_diff):
                closest_sum = current_sum
                result = [a, b]
                max_abs_diff = b - a

            # Adjust pointers
            if current_sum <= target:
                left += 1  # Try for a larger sum
            else:
                right -= 1  # Try for a smaller sum

        return result
