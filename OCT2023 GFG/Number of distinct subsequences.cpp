class Solution:
	def distinctSubsequences(self, S):
		# code here
		mod = 10**9 + 7
        n = len(S)

        # Initialize a dp array to store the number of distinct subsequences
        dp = [0] * (n + 1)

        # Empty subsequence is always a valid subsequence
        dp[0] = 1

        # Create a dictionary to store the last position of each character
        last_pos = {}

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod  # Doubling the previous result

            # If the current character has appeared before
            if S[i - 1] in last_pos:
                # Subtract the number of subsequences that end at the previous occurrence of this character
                dp[i] = (dp[i] - dp[last_pos[S[i - 1]]] + mod) % mod

            # Update the last position of the current character
            last_pos[S[i - 1]] = i

        # Subtract 1 to exclude the empty subsequence
        return (dp[n] - 1) % mod
