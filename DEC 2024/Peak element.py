class Solution:
    def peakElement(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
                return mid
            
            # If left neighbor is greater, move to the left half
            if mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                # Otherwise, move to the right half
                low = mid + 1
        
        return -1  # This case won't occur due to constraints in the problem

# Function to validate the output
def validate_peak(arr, index):
    n = len(arr)
    if index < 0 or index >= n:
        return False
    if (index > 0 and arr[index] <= arr[index - 1]) or (index < n - 1 and arr[index] <= arr[index + 1]):
        return False
    return True
