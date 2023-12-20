class Solution:
    def findWinner(self, n, A):
        xor = 0
        for num in A:
            xor ^= num

        if xor == 0:
            return 1

        return 1 if n % 2 == 0 else 2
