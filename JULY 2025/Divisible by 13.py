class Solution:
    def divby13(self, s):
        rem = 0
        for digit in s:
            rem = (rem * 10 + int(digit)) % 13
        return rem == 0
