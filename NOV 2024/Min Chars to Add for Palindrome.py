class Solution:
    def minChar(self, s):
        # Function to compute LPS array
        def computeLPSArray(string):
            n = len(string)
            lps = [0] * n
            length = 0
            i = 1
            while i < n:
                if string[i] == string[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        # Generate the concatenated string
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        lps = computeLPSArray(combined)
        
        # Minimum characters to add
        return len(s) - lps[-1]
