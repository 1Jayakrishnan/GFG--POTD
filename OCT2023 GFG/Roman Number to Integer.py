class Solution:
    def romanToDecimal(self, S): 
        # code here
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_value = 0

        # Start from the right side of the string
        for char in S[::-1]:
            value = roman_values[char]

            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                result -= value
            else:
                result += value

            prev_value = value

        return result
