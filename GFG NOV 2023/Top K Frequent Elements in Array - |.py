from collections import Counter
class Solution:
	def topK(self, nums, k):
		#Code here
		counts = Counter(nums)
        
        # Sort the elements by frequency (descending) and then by value (descending)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
        
        # Extract the top k elements from the sorted list
        result = [x[0] for x in sorted_counts[:k]]
        
        return result
