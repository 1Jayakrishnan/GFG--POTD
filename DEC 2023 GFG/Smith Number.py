import math

class Solution:
    def is_prime(self, n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(self, n):
        _sum = 0
        while n:
            _sum += n % 10
            n //= 10
        return _sum

    def sum_of_prime_factor(self, n):
        f = 1
        _sum = 0
        while n > 1:
            f += 1
            if not self.is_prime(f):
                continue
            while n % f == 0:
                _sum += self.sum_of_digits(f)
                n //= f
        return _sum

    def smithNum(self, n):
        if self.is_prime(n):
            return 0
        return 1 if self.sum_of_prime_factor(n) == self.sum_of_digits(n) else 0
