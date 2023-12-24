from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        prices_with_days = [(price[i], i + 1) for i in range(n)]
        
        # Sort the list based on prices in ascending order
        prices_with_days.sort(key=lambda x: x[0])

        # Initialize variables to keep track of the total number of stocks bought and the remaining money
        total_stocks_bought = 0
        remaining_money = k

        # Iterate through the sorted list of prices
        for p, day in prices_with_days:
            # Calculate the maximum number of stocks that can be bought on the current day
            max_stocks = min(day, remaining_money // p)

            # Update the total number of stocks bought and remaining money
            total_stocks_bought += max_stocks
            remaining_money -= max_stocks * p

        return total_stocks_bought
        
