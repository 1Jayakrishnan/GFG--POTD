class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [-1] * (n + 1)
        dp[0] = 0  # Base case: 0 length segment yields 0 cuts
        
        # Iterate through each length from 1 to n
        for i in range(1, n + 1):
            # If the length can be obtained by making a cut of length x
            if i >= x and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
            
            # If the length can be obtained by making a cut of length y
            if i >= y and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
                
            # If the length can be obtained by making a cut of length z
            if i >= z and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)
        
        # If dp[n] is still -1, it means it's not possible to cut the segment into the given lengths
        return dp[n] if dp[n] != -1 else 0
