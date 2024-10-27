class Solution:
    def findTriplet(self, arr):
        # Sort the array to allow two-pointer technique
        arr.sort()
        n = len(arr)
        
        # Traverse the array with one element fixed
        for i in range(n - 1, 1, -1):  # Start from the largest element
            target = arr[i]
            left, right = 0, i - 1
            
            # Use two-pointer approach to find two numbers that sum to the target
            while left < right:
                sum_lr = arr[left] + arr[right]
                
                if sum_lr == target:
                    return True
                elif sum_lr < target:
                    left += 1
                else:
                    right -= 1
        
        return False
