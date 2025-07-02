from collections import defaultdict

class Solution:
    def totalElements(self, arr):
        left = 0
        freq = defaultdict(int)
        max_len = 0

        for right in range(len(arr)):
            freq[arr[right]] += 1

            # Shrink window if more than 2 distinct elements
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
