class Solution:
	def TotalWays(self, N):
		# Code here
        mod = 10**9 + 7

        curr = prev = 1

        for i in range(1, N + 1):
            next_val = (curr + prev) % mod
            prev = curr
            curr = next_val

        return (curr * curr) % mod
