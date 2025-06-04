class Solution:
    def lcsOf3(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        # Use two layers to save space
        dp = [[[0 for _ in range(n3+1)] for _ in range(n2+1)] for _ in range(2)]
        
        for i in range(1, n1+1):
            curr = i % 2
            prev = (i - 1) % 2
            for j in range(1, n2+1):
                for k in range(1, n3+1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        dp[curr][j][k] = 1 + dp[prev][j-1][k-1]
                    else:
                        dp[curr][j][k] = max(
                            dp[prev][j][k],
                            dp[curr][j-1][k],
                            dp[curr][j][k-1]
                        )
        
        return dp[n1 % 2][n2][n3]
