class Solution:
    def search(self, pat, txt):
        # code here
        # Result list to store the starting indices of matches
        result = []
        
        # Length of the pattern and text
        m, n = len(pat), len(txt)
        
        # Iterate through the text, checking substrings of length equal to the pattern
        for i in range(n - m + 1):  # Loop till `n - m` so we don't exceed the length
            if txt[i:i + m] == pat:
                result.append(i)
        
        return result
