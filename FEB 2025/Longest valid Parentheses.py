class Solution:
    def maxLength(self, s):
        # code here
        stack = [-1]  # Initialize the stack with base index -1
        max_length = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)  # Push the index of '('
            else:
                stack.pop()  # Pop for ')'
                if not stack:
                    # If stack is empty, push the current index as base for next valid substring
                    stack.append(i)
                else:
                    # Current valid substring length is i - stack[-1]
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
