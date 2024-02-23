from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        if n < 2:
            return 0

        # Initialize arrays to store the maximum profit at each step
        profit_first_transaction = [0] * n
        profit_second_transaction = [0] * n

        # Calculate maximum profit for the first transaction
        min_price = price[0]
        for i in range(1, n):
            min_price = min(min_price, price[i])
            profit_first_transaction[i] = max(profit_first_transaction[i - 1], price[i] - min_price)

        # Calculate maximum profit for the second transaction
        max_price = price[n - 1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, price[i])
            profit_second_transaction[i] = max(profit_second_transaction[i + 1], max_price - price[i])

        # Calculate the overall maximum profit by combining the two transactions
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, profit_first_transaction[i] + profit_second_transaction[i])

        return max_profit
