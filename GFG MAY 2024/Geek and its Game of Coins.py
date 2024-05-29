class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        dp = [False] * (n+1)
        for i in range(1,len(dp)):
            os = i-1
            xs = i-x
            ys = i-y
            ans = dp[os]
            if(xs>=0):
                ans = ans and dp[xs]
            if(ys>=0):
                ans = ans and dp[ys]
            dp[i] = not ans
        return int(dp[-1])
