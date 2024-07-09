class Solution:
    def threeSumClosest(self, arr, target):
        # Sort the array
        arr.sort()
        n = len(arr)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                # If current sum is closer to the target, update closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                elif abs(current_sum - target) == abs(closest_sum - target) and current_sum > closest_sum:
                    closest_sum = current_sum
                
                # Move the pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # If the sum is exactly the target, return it immediately
        
        return closest_sum
