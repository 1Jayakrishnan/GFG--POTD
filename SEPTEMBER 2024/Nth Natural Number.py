class Solution:
    def findNth(self, n):
        result = 0
        power = 1

        # Convert the number to base-9 equivalent
        while n > 0:
            result += (n % 9) * power
            n //= 9
            power *= 10

        return result
