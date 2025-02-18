import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        max_heap = []
        
        # Process each point.
        for x, y in points:
            # Compute the squared Euclidean distance.
            dist_sq = x * x + y * y
            # Push negative distance to simulate max-heap.
            heapq.heappush(max_heap, (-dist_sq, [x, y]))
            # If heap size exceeds k, remove the farthest point.
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # The heap now contains k closest points.
        # Extract the points from the heap (order does not matter).
        return [point for (_, point) in max_heap]
        
