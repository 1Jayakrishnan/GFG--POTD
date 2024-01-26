class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        # Calculate value-to-weight ratio for each item and store it in a list.
        ratios = [(item.value / item.weight, item) for item in arr]

        # Sort the items based on their value-to-weight ratios in descending order.
        ratios.sort(reverse=True, key=lambda x: x[0])

        # Initialize variables to keep track of total value and remaining capacity.
        total_value = 0
        remaining_capacity = W

        # Loop through the sorted items and add them to the knapsack.
        for ratio, item in ratios:
            # If the entire item can be added, add it and update remaining capacity.
            if remaining_capacity >= item.weight:
                total_value += item.value
                remaining_capacity -= item.weight
            else:
                # If the entire item can't be added, add a fraction of it.
                fraction = remaining_capacity / item.weight
                total_value += fraction * item.value
                break  # Knapsack is full, exit the loop.

        return total_value
