class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff = [a1[i] - a2[i] for i in range(n)]
        
        prefix_sum = 0
        max_len = 0
        first_occurrence = {0: -1}  # sum 0 occurs before index 0
        
        for i in range(n):
            prefix_sum += diff[i]
            if prefix_sum in first_occurrence:
                span = i - first_occurrence[prefix_sum]
                max_len = max(max_len, span)
            else:
                first_occurrence[prefix_sum] = i
        
        return max_len
