class Solution:
    def minRemoval(self, intervals):
        # Code here
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        removal_count = 0
        last_end = float('-inf')  # Initialize last_end to a very small value
        
        for start, end in intervals:
            if start < last_end:
                # Overlapping interval, increment removal count
                removal_count += 1
            else:
                # No overlap, update last_end
                last_end = end
        
        return removal_count
