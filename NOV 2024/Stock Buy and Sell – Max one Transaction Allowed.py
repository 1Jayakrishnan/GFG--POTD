class Solution:
    def maximumProfit(self, prices):
        # If there are less than 2 prices, no profit can be made
        if not prices or len(prices) < 2:
            return 0
        
        # Initialize variables
        min_price = float('inf')  # Start with a very high minimum price
        max_profit = 0  # Start with zero profit
        
        # Iterate through the prices
        for price in prices:
            # Update minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate profit and update max profit if it's higher
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
