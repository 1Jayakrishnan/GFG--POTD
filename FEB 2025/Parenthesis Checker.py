class Solution:
    def isBalanced(self, s):
        # code here
        # Dictionary to map closing brackets to their corresponding opening brackets.
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            # If the character is an opening bracket, push it onto the stack.
            if char in bracket_map.values():
                stack.append(char)
            # If it's a closing bracket, check if it matches the top of the stack.
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # If the character is not a bracket, you can choose to ignore it or handle it.
                # For this problem, we assume the string contains only bracket characters.
                pass
        
        # If the stack is empty, then all brackets matched correctly.
        return len(stack) == 0
