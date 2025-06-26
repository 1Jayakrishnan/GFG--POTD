class Solution:
    def minValue(self, s, k):
        freq = [0] * 26
        for c in s: freq[ord(c) - ord('a')] += 1
        
        count = [0] * (len(s) + 1)
        for f in freq: 
            if f: count[f] += 1
                
        for f in range(len(s), 0, -1):
            while k and count[f]:
                take = min(k, count[f])
                count[f] -= take
                count[f - 1] += take
                k -= take
        
        return sum(f * f * c for f, c in enumerate(count))
