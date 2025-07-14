class Solution:
    def cuts(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # base case: empty prefix requires 0 cuts

        def is_power_of_five(x):
            if x == 0:
                return False
            while x % 5 == 0:
                x //= 5
            return x == 1

        for i in range(1, n + 1):
            for j in range(i):
                substr = s[j:i]
                if substr[0] == '0':  # leading zeros are invalid
                    continue
                val = int(substr, 2)
                if is_power_of_five(val):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1
