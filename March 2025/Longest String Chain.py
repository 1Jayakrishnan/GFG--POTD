class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)  # Step 1: Sort words by length
        dp = {}  # Dictionary to store longest chain for each word
        max_chain_length = 1  # At minimum, a single word is a valid chain

        for word in words:
            dp[word] = 1  # Initialize the word chain length as 1
            
            # Try removing each character to form a possible predecessor
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]  # Remove the i-th character
                
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)

            max_chain_length = max(max_chain_length, dp[word])  # Update global max

        return max_chain_length
