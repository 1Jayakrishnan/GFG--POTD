class Solution:
    def myAtoi(self, s):
        # Define integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Strip leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Handle optional sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3: Convert characters to integer
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = ord(s[index]) - ord('0')  # Convert character to integer
            result = result * 10 + digit
            index += 1

            # Check for overflow
            if result * sign > INT_MAX:
                return INT_MAX
            if result * sign < INT_MIN:
                return INT_MIN

        # Step 4: Apply the sign
        return result * sign
