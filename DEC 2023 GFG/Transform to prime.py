class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    def minNumber(self, arr,n):
        # code here
        array_sum = sum(arr)

        # Step 2: Check if the sum is already a prime number
        if self.is_prime(array_sum):
            return 0  # No insertion needed, the sum is already prime

        # Step 3: Find the minimum non-negative number to be inserted
        current_sum = array_sum
        while not self.is_prime(current_sum):
            current_sum += 1

        return current_sum - array_sum
