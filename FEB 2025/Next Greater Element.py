class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        result = [-1] * n  # Initialize result array with -1
        stack = []  # Monotonic decreasing stack

        for i in range(n - 1, -1, -1):  # Traverse from right to left
            while stack and stack[-1] <= arr[i]:  
                stack.pop()  # Remove elements that are smaller than the current element
            
            if stack:  # If stack is not empty, top is the next greater element
                result[i] = stack[-1]

            stack.append(arr[i])  # Push the current element onto stack
        
        return result
