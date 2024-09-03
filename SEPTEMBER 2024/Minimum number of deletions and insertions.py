class Solution:
	def minOperations(self, str1, str2):
		# code here
		len1, len2 = len(str1), len(str2)
        # Create a 2D array (table) to store lengths of longest common suffixes
        # Initialize all entries as 0
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
       
        return len1+len2 -2*dp[len1][len2]
