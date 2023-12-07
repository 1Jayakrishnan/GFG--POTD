class Solution:
    def countSubarrays(self, a,n,L,R): 
        # Complete the function
        out = 0
        range_size = 0
        i = 0

        for j in range(n):
            if L <= a[j] <= R:
                range_size = j - i + 1
            elif a[j] > R:
                range_size = 0
                i = j + 1

            out += range_size

        return out
