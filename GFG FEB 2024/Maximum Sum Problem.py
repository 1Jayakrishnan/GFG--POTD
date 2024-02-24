class Solution:
    def maxSum(self, n): 
        # code here 
        memo = {}

        def calculate_max_sum(num):
            if num in memo:
                return memo[num]

            if num == 0:
                return 0

            max_sum = max(
                num,
                calculate_max_sum(num // 2) + calculate_max_sum(num // 3) + calculate_max_sum(num // 4)
            )

            memo[num] = max_sum
            return max_sum

        return calculate_max_sum(n)


