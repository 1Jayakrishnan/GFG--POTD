class Solution:
    def betterString(self, str1, str2):
        # Code here
        def count_subsequences(s):
            mod = 10**9 + 7
            n = len(s)
            
            # dp[i] stores the count of distinct subsequences ending at s[i]
            dp = [0] * (n + 1)
            
            # Empty subsequence has one occurrence
            dp[0] = 1
            
            # Map to store the last index of each character in the string
            last_index = {}
            
            for i in range(1, n + 1):
                dp[i] = (2 * dp[i - 1]) % mod
                
                # If the current character has appeared before
                if s[i - 1] in last_index:
                    dp[i] = (dp[i] - dp[last_index[s[i - 1]] - 1] + mod) % mod
                
                # Update the last index of the current character
                last_index[s[i - 1]] = i
            
            return dp[n] - 1  # Subtract 1 to exclude the empty subsequence
        
        # Count distinct subsequences for both strings
        count1 = count_subsequences(str1)
        count2 = count_subsequences(str2)
        
        # Return the better string based on the counts
        if count1 > count2:
            return str1
        elif count1 < count2:
            return str2
        else:
            return str1  
