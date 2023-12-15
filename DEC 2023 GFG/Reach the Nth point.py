class Solution:
    def nthPoint(self, n):
        num1, num2, mod = 1, 1, 10**9 + 7

        for i in range(1, n):
            a = (num1 + num2) % mod
            num1, num2 = num2, a

        return num2
