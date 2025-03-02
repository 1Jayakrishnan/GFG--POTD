from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        if k == 1:
            return arr  # If window size is 1, each element is its own maximum.

        result = []
        dq = deque()  # Stores indices of useful elements

        for i in range(n):
            # Remove elements that are out of this window (leftmost elements)
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove smaller elements from the back (they will never be needed)
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            # Add current element index to deque
            dq.append(i)

            # Collect results only after the first k elements
            if i >= k - 1:
                result.append(arr[dq[0]])  # Max of current window

        return result
