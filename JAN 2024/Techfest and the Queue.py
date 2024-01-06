from typing import List

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        def sieve(max_val):
            primes = [True] * (max_val + 1)
            primes[0] = primes[1] = False
            for i in range(2, int(max_val**0.5) + 1):
                if primes[i]:
                    for j in range(i * i, max_val + 1, i):
                        primes[j] = False
            return [num for num in range(max_val + 1) if primes[num]]

        def prime_factors(n, primes):
            factors = []
            for prime in primes:
                if prime * prime > n:
                    break
                while n % prime == 0:
                    factors.append(prime)
                    n //= prime
            if n > 1:
                factors.append(n)
            return factors

        max_val = int(b**0.5) + 1
        primes = sieve(max_val)

        memo = {}  # Memoization for sum of powers

        total_points = 0
        for ticket_number in range(a, b + 1):
            factors = prime_factors(ticket_number, primes)
            unique_factors = set(factors)

            if tuple(factors) in memo:
                total_points += memo[tuple(factors)]
            else:
                power_sum = sum(factors.count(factor) for factor in unique_factors)
                total_points += power_sum
                memo[tuple(factors)] = power_sum

        return total_points


