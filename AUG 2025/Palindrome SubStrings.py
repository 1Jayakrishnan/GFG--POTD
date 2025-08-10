class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        
        # helper to expand around a given center
        def expand(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= 2:
                    count += 1
                l -= 1
                r += 1
        
        for i in range(n):
            # Odd-length palindromes (center at i)
            expand(i, i)
            # Even-length palindromes (center between i and i+1)
            expand(i, i + 1)
        
        return count
