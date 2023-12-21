class Solution:
    def minCandy(self, N, ratings):
        # Code here
        if not ratings or N == 0:
            return 0

        candies = [1] * N  # Initialize candies array with 1 for each child

        # Left-to-Right pass
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-Left pass
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Sum up the candies array to get the total minimum candies needed
        return sum(candies)
