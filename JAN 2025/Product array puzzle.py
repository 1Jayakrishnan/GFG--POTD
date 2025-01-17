class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        if n == 1:
            return []
        
        # Initialize result array with 1s
        res = [1] * n
        
        # Calculate prefix product for each index
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
        
        # Calculate suffix product and update result array
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
        
        return res
