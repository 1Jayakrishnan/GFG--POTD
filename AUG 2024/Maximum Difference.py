class Solution:
    def findMaxDiff(self, arr):
        # code here
        n = len(arr)
        
        # Initialize left and right smaller arrays
        left_smaller = [0] * n
        right_smaller = [0] * n
        
        # Stack for finding the nearest smaller to left
        stack = []
        
        # Fill left_smaller array
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                left_smaller[i] = stack[-1]
            else:
                left_smaller[i] = 0
            stack.append(arr[i])
        
        # Clear stack to reuse for finding the nearest smaller to right
        stack.clear()
        
        # Fill right_smaller array
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                right_smaller[i] = stack[-1]
            else:
                right_smaller[i] = 0
            stack.append(arr[i])
        
        # Find the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(left_smaller[i] - right_smaller[i]))
        
        return max_diff
