class Solution:
    def caseSort(self, s):
        upper = sorted([c for c in s if c.isupper()])
        lower = sorted([c for c in s if c.islower()])
        
        result = []
        i = j = 0  # i for lower, j for upper
        
        for ch in s:
            if ch.isupper():
                result.append(upper[j])
                j += 1
            else:
                result.append(lower[i])
                i += 1
        
        return ''.join(result)
