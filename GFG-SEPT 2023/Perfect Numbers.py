import math
class Solution:
    def isPerfectNumber(self, N):
        # code here
        if N <= 1:
           return 0

        sum_of_factors = 1  # Start with 1 as 1 is always a factor

        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                sum_of_factors += i
                # If i is not the square root of N, add its pair factor as well
                if i != N // i:
                    sum_of_factors += N // i
    
        if sum_of_factors == N:
            return 1
        else:
            return 0
