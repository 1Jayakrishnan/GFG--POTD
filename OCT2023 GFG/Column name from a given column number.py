class Solution:
    def colName(self, n):
        # your code here
        column_title = ""
        
        while n > 0:
            n -= 1  # Decrement by 1 to handle 0-based indexing
            remainder = n % 26  # Get the remainder when divided by 26
            column_title = chr(ord('A') + remainder) + column_title
            n //= 26  # Integer division by 26
            
        return column_title
