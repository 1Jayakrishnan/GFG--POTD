import heapq

class Solution:
    def getMedian(self, arr):
        # left will be a max-heap (we store negative values)
        left = []  
        # right will be a min-heap
        right = []  
        medians = []
        
        for num in arr:
            # Insert into appropriate heap.
            if not left or num <= -left[0]:
                heapq.heappush(left, -num)
            else:
                heapq.heappush(right, num)
            
            # Balance the heaps so that:
            # left has either the same number of elements as right or one more.
            if len(left) > len(right) + 1:
                heapq.heappush(right, -heapq.heappop(left))
            elif len(right) > len(left):
                heapq.heappush(left, -heapq.heappop(right))
            
            # Compute the median based on the sizes.
            if len(left) > len(right):
                median = float(-left[0])
            else:
                median = (-left[0] + right[0]) / 2.0
            
            medians.append(median)
        
        return medians
