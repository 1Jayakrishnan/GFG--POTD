class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        max_len = 0
        prefix_index_map = {}

        for i in range(n):
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum > 0:
                max_len = i + 1  # whole array from 0 to i is valid
            elif (prefix_sum - 1) in prefix_index_map:
                length = i - prefix_index_map[prefix_sum - 1]
                max_len = max(max_len, length)

            if prefix_sum not in prefix_index_map:
                prefix_index_map[prefix_sum] = i  # store earliest index

        return max_len
