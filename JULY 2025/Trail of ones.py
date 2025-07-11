class Solution:
    def countConsec(self, n: int) -> int:
        if n == 0:
            return 0

        a, b = 1, 1  # a = end with 0, b = end with 1

        for i in range(2, n + 1):
            new_a = a + b
            new_b = a
            a, b = new_a, new_b

        no_consec_ones = a + b
        total = 1 << n  # 2^n using bit shift

        return total - no_consec_ones
