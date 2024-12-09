class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        result = []
        i = 0
        n = len(intervals)

        # Add intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged newInterval
        result.append(newInterval)

        # Add intervals that come after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
