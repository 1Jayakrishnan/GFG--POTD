import heapq

class Solution:
    def nearlySorted(self, arr, k):
        # Initialize the min-heap with the first k+1 elements
        min_heap = arr[:k + 1]
        heapq.heapify(min_heap)  # Create a min-heap from the first k+1 elements
        
        # Initialize an index for the result array to keep sorted elements in place
        result_index = 0

        # Process the remaining elements of the array
        for i in range(k + 1, len(arr)):
            # Place the smallest element from heap to the result position
            arr[result_index] = heapq.heappop(min_heap)
            result_index += 1
            
            # Push the current element to the heap
            heapq.heappush(min_heap, arr[i])

        # Extract remaining elements from the heap and place in result positions
        while min_heap:
            arr[result_index] = heapq.heappop(min_heap)
            result_index += 1

        return arr
