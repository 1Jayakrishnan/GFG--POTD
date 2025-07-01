from collections import defaultdict

class Solution:
    def substrCount(self, s, k):
        n = len(s)
        if k > n:
            return 0

        freq = defaultdict(int)
        count = 0
        distinct = 0

        for i in range(n):
            # Add new character
            if freq[s[i]] == 0:
                distinct += 1
            freq[s[i]] += 1

            # Remove character going out of window
            if i >= k:
                freq[s[i - k]] -= 1
                if freq[s[i - k]] == 0:
                    distinct -= 1

            # When window is of size k, check for condition
            if i >= k - 1:
                if distinct == k - 1:
                    count += 1

        return count
