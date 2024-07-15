class Solution:
    def smallestNumber(self, s, d):
        # code here
        # Step 1: Check if the problem is solvable
        if s > 9 * d or (s == 0 and d > 1):
            return -1
    
        # Step 2: Initialize the digits array
        digits = [0] * d
    
        # Step 3: Fill the digits array from right to left
        for i in range(d - 1, -1, -1):
            if s > 9:
                digits[i] = 9
                s -= 9
            else:
                digits[i] = s
                s = 0
    
        # Step 4: Adjust the leading zero if necessary
        if digits[0] == 0:
            digits[0] = 1
            for i in range(1, d):
                if digits[i] > 0:
                    digits[i] -= 1
                    break
    
        # Step 5: Convert the digits array to a string and return it
        result = ''.join(map(str, digits))
        return result
