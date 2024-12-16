
class Solution:
    def kthElement(self, a, b, k):
        new = sorted(a+b)
        
        return new[k-1]
