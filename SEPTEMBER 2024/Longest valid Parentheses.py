class Solution:
    def maxLength(self, string):
        # code here
        stack = [-1]  # To store indices of parentheses
        count = 0
        
        for i, char in enumerate(string):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the last index (matching opening parenthesis)
                
                if not stack:
                    # If stack becomes empty, push the current index as a base for future valid substrings
                    stack.append(i)
                else:
                    # Calculate the length of the valid substring by using the top of the stack
                    count = max(count, i - stack[-1])
        
        return count 
