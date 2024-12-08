class Solution:
	def mergeOverlap(self, arr):
		#Code here
		# Sort intervals based on the start time
        arr.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in arr:
            # If merged list is empty or intervals do not overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the intervals by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
