class Solution:
    def minOperation(self, n):
        out = -1
        while n:
            if n % 2:
                out += 1
            n //= 2
            out += 1

        return out
