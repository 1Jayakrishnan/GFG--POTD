class Solution:
    def countPairs(self, arr, target):
        # Sort the array first
        arr.sort()
        count = 0
        i = 0
        j = len(arr) - 1
        
        # Two-pointer approach
        while i < j:
            if arr[i] + arr[j] < target:
                # If arr[i] + arr[j] is less than the target, then all pairs
                # with arr[i] and arr[k] (where i < k < j) will also be valid.
                count += (j - i)
                i += 1  # Move the left pointer to the right
            else:
                j -= 1  # Move the right pointer to the left
                
        return count
