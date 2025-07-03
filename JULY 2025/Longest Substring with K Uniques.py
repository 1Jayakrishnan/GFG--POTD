from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        left = 0
        max_len = -1
        char_freq = defaultdict(int)

        for right in range(n):
            char_freq[s[right]] += 1

            # Shrink window if more than k distinct chars
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1

            # Check if exactly k distinct characters
            if len(char_freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len
