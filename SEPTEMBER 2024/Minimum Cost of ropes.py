import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr):
        
        if len(arr) == 1:
            return 0
        
        #convert the array to min-heap
        heapq.heapify(arr)
        
        total_cost = 0
        
        
        while len(arr) > 1:
        
            first_min = heapq.heappop(arr)
            second_min = heapq.heappop(arr)
            
            cost = first_min + second_min
            
            total_cost += cost 
            
            #push the cost to the arr
            
            heapq.heappush(arr, cost)
            
            
        return total_cost
