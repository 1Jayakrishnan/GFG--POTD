class Solution:
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = []
        bracket_map = { ')':'(', '}':'{', ']':'['}
        
        for char in x:
            if char in '({[':
                stack.append(char)
            elif char in')}]':
                #check stack is empty or not
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return 0
            
       # If stack is empty, all brackets are balanced
        return len(stack) == 0
