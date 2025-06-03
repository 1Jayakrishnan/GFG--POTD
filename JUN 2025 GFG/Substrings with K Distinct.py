class Solution:
    def countSubstr(self, s, k):
        def countAtMostK(s, k):
            from collections import defaultdict
            freq = defaultdict(int)
            left = 0
            count = 0
            for right in range(len(s)):
                freq[s[right]] += 1
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                count += (right - left + 1)
            return count
        
        return countAtMostK(s, k) - countAtMostK(s, k - 1)
