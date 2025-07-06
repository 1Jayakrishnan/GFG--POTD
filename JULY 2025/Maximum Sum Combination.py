import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        n = len(a)
        a.sort(reverse=True)
        b.sort(reverse=True)
        
        maxHeap = []
        visited = set()
        
        # Initialize with the largest sum
        heapq.heappush(maxHeap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))
        
        result = []
        
        while k > 0 and maxHeap:
            curr_sum, i, j = heapq.heappop(maxHeap)
            result.append(-curr_sum)
            k -= 1
            
            # Push next pair (i+1, j)
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(maxHeap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))
            
            # Push next pair (i, j+1)
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(maxHeap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))
        
        return result
