class Solution:
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        span = [0] * n  # To store the span for each day
        stack = []  # Stack to keep track of indices
        
        for i in range(n):
            # Pop indices from the stack while the current element is greater than
            # or equal to the element at the index stored on the top of the stack.
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            # If stack is empty, current price is greater than all elements to its left.
            if not stack:
                span[i] = i + 1
            else:
                # Else, the span is the difference between current index and the index on top of the stack.
                span[i] = i - stack[-1]
            
            # Push this index onto the stack.
            stack.append(i)
        
        return span
