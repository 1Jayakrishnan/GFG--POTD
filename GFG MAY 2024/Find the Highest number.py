from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        left, right = 0, len(a) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if a[mid] < a[mid + 1]:
                # Peak is in the right half
                left = mid + 1
            else:
                # Peak is in the left half or it is the mid itself
                right = mid
        
        # Left should be the peak element index
        return a[left]
