from math import factorial

class Solution:
    def nCr(self, n, r):
        # code here
        if r > n:
            return 0
        
        ans = (factorial(n)//(factorial(r) * factorial(n-r)))
        
        return ans
