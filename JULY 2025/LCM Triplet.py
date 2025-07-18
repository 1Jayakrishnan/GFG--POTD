import math

class Solution:
    def lcmTriplets(self, n):
        def lcm(a, b):
            return a * b // math.gcd(a, b)

        def lcm3(a, b, c):
            return lcm(lcm(a, b), c)

        if n <= 2:
            return n
        elif n == 3:
            return 6
        elif n % 2 != 0:
            return n * (n - 1) * (n - 2)
        elif n % 3 != 0:
            return n * (n - 1) * (n - 3)
        else:
            return max(
                lcm3(n, n - 1, n - 2),
                lcm3(n - 1, n - 2, n - 3)
            )
