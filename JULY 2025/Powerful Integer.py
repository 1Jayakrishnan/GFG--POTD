class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict

        changes = defaultdict(int)

        # Step 1: Record all start and end points
        for start, end in intervals:
            changes[start] += 1
            changes[end + 1] -= 1

        # Step 2: Sort all the keys (events)
        points = sorted(changes)
        active = 0
        max_powerful = -1

        for i in range(len(points) - 1):
            active += changes[points[i]]
            # If the active count is ≥ k, all integers in this range are powerful
            if active >= k:
                # Take the rightmost integer in this range
                max_powerful = max(max_powerful, points[i + 1] - 1)

        return max_powerful
