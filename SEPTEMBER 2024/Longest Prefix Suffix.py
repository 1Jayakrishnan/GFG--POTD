class Solution:
    def lps(self, string):
        n = len(string)
        lps = [0] * n  # Array to store the longest prefix suffix values
        length = 0  # Length of the previous longest prefix suffix
        i = 1
        
        # The loop calculates the lps array for the string
        while i < n:
            if string[i] == string[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                # If there is a mismatch, fall back to the previous lps value
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # The last value of the lps array contains the result
        return lps[n - 1]
