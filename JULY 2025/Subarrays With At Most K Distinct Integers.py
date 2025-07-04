from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):
        freq = defaultdict(int)
        left = 0
        res = 0
        distinct = 0

        for right in range(len(arr)):
            if freq[arr[right]] == 0:
                distinct += 1
            freq[arr[right]] += 1

            while distinct > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct -= 1
                left += 1

            # Add all subarrays ending at `right` with ≤ k distinct
            res += (right - left + 1)

        return res
