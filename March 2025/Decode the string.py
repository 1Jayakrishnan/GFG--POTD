class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                # Build the current number (may have multiple digits)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current string and current number onto the stack
                stack.append((current_str, current_num))
                # Reset for the new substring inside the brackets
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop the last string and number from the stack
                prev_str, num = stack.pop()
                # Build the new string: previous string + (current_str repeated num times)
                current_str = prev_str + current_str * num
            else:
                # It's a letter; append to current string.
                current_str += char
        
        return current_str
        
