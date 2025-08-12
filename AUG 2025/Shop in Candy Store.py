class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        n = len(prices)

        # Minimum cost
        min_cost = 0
        i, j = 0, n - 1
        while i <= j:
            min_cost += prices[i]
            i += 1
            j -= k  # get k most expensive candies for free

        # Maximum cost
        max_cost = 0
        i, j = 0, n - 1
        while i <= j:
            max_cost += prices[j]
            j -= 1
            i += k  # get k cheapest candies for free

        return [min_cost, max_cost]
