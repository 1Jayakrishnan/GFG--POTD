class Solution:   
    def peakElement(self,arr, n):
        # Code here
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if arr[mid] is a peak element
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return mid  # Return the index where the peak element is found
            
            # If the element to the left of mid is greater, search in the left subarray
            if mid > 0 and arr[mid - 1] > arr[mid]:
                right = mid - 1
            else:
                # Otherwise, search in the right subarray
                left = mid + 1
        
        return -1  # No peak element found
