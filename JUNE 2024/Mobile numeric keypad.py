class Solution:
	def getCount(self, n):
		# code here
		if n == 1:
            return 10  # Each digit (0-9) is a valid sequence of length 1.

        # Neighbors represent the allowed moves for each digit
        neighbors = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }
        
        # Initialize dp array
        dp = [[0] * 10 for _ in range(n + 1)]
        
        # Base case: There's one way to have a sequence of length 1 for each digit
        for i in range(10):
            dp[1][i] = 1
        
        # Fill dp array for lengths from 2 to n
        for length in range(2, n + 1):
            for digit in range(10):
                dp[length][digit] = 0
                for neighbor in neighbors[digit]:
                    dp[length][digit] += dp[length - 1][neighbor]
        
        # Sum up all sequences of length n
        result = sum(dp[n][digit] for digit in range(10))
        
        return result
