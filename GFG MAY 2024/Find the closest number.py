
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        if n == 1:
            return arr[0]
        
        # Helper function to perform binary search
        def binary_search(arr, k):
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    return mid
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
        # Find the position where k would be inserted
        pos = binary_search(arr, k)
        
        # If pos is 0, it means k is smaller than all elements
        if pos == 0:
            return arr[0]
        # If pos is n, it means k is larger than all elements
        if pos == n:
            return arr[-1]
        
        # Compare arr[pos] with its previous element arr[pos - 1]
        if abs(arr[pos] - k) < abs(arr[pos - 1] - k):
            return arr[pos]
        elif abs(arr[pos] - k) > abs(arr[pos - 1] - k):
            return arr[pos - 1]
        else:
            # If the differences are the same, return the greater value
            return max(arr[pos], arr[pos - 1])
