class Solution:
    def findExtra(self, n, arr1, arr2):
        #add code here
        low, high = 0, n - 2  # Since arr2 is of size n-1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if this is the point of divergence
            if arr1[mid] == arr2[mid]:
                # If same, the extra element must be further in arr1
                low = mid + 1
            else:
                # Otherwise, the extra element must be before or at mid
                high = mid - 1
        
        # When low exceeds high, the position low will be the extra element
        return low
