class Solution:
    def countValid(self, n, arr):
        arr_set = set(arr)
        all_digits = set(range(10))
        allowed_digits = list(all_digits - arr_set)
        k = len(allowed_digits)
        
        if k == 0:
            return 9 * 10**(n - 1) if n > 1 else 9  # all numbers contain a digit from arr

        # Count of n-digit numbers without using any digit from arr
        count = 0
        if n == 1:
            count = k - (1 if 0 in allowed_digits else 0)
        else:
            # First digit cannot be 0
            first_digit_choices = k - (1 if 0 in allowed_digits else 0)
            count = first_digit_choices * (k ** (n - 1))

        total_n_digit_numbers = 9 * 10**(n - 1) if n > 1 else 9
        return total_n_digit_numbers - count
