class Solution:
    def series(self, n):
        # Code here
        MOD = 10**9 + 7

        # Initialize the first two Fibonacci numbers
        fib = [0] * (n + 1)
        fib[0], fib[1] = 0, 1

        # Calculate Fibonacci numbers modulo MOD
        for i in range(2, n + 1):
            fib[i] = (fib[i - 1] + fib[i - 2]) % MOD

        return fib
