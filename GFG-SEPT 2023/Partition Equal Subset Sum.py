class Solution:
    def equalPartition(self, N, arr):
        # code here
        total_sum = sum(arr)

        # If the total sum is odd, it can't be divided into two equal parts
        if total_sum % 2 != 0:
            return 0

        half_sum = total_sum // 2

        # Create a 2D DP array to store whether a subset sum is achievable
        dp = [[False] * (half_sum + 1) for _ in range(N + 1)]

        # Base case: If the sum is 0, it can always be achieved by choosing an empty subset
        for i in range(N + 1):
            dp[i][0] = True

        # Fill the DP table
        for i in range(1, N + 1):
            for j in range(1, half_sum + 1):
                # If the current element is greater than the current sum, exclude it
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # Otherwise, consider including or excluding the current element
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

        # The last cell of the DP table will tell us if it's possible to partition the array
        return 1 if dp[N][half_sum] else 0
