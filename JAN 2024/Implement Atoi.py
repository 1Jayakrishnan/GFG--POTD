class Solution:
    def atoi(self, s):
        if not s:
            return -1  # Empty string, conversion not feasible

        sign = 1
        result = 0
        i = 0

        # Check for the sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Iterate through the string
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Check for non-numeric characters
        if i < len(s) and not s[i].isdigit():
            return -1

        # Apply the sign
        result *= sign

        # Check for overflow (optional step)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = min(max(result, INT_MIN), INT_MAX)

        return result
