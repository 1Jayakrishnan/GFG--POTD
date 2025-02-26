class Solution:
    def maxOfMins(self, arr):
       # code here
        n = len(arr)
        # Arrays to store indexes of previous and next smaller elements
        left = [-1] * n   # Previous smaller: index of previous element smaller than arr[i]
        right = [n] * n   # Next smaller: index of next element smaller than arr[i]
        
        # Compute Previous Smaller for each element
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Compute Next Smaller for each element
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Initialize result array for window sizes 1 to n.
        # We use an array of size n+1 so that res[w] corresponds to window size w.
        res = [0] * (n + 1)
        
        # For every element, find the window size in which it is the minimum,
        # then update the result for that window size.
        for i in range(n):
            window_size = right[i] - left[i] - 1
            res[window_size] = max(res[window_size], arr[i])
        
        # Fill the result array: if for a window size w the answer is not computed,
        # then take the maximum from a larger window.
        for w in range(n - 1, 0, -1):
            res[w] = max(res[w], res[w + 1])
        
        # Return the answers for window sizes from 1 to n.
        return res[1:]

