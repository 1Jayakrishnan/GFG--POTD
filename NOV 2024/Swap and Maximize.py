class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        rearranged = []
        left=0
        right=len(arr)-1
        
        while left<=right:
            if left < right:
                rearranged.append(arr[left])
                rearranged.append(arr[right])
            else:
                rearranged.append(arr[left])
            left += 1 
            right -= 1    
        #print(rearranged)
        
        total = 0
        for i in range(len(rearranged)-1):
            total += abs(rearranged[i]-rearranged[i+1])
        
        cycle = abs(rearranged[len(arr)-1] - rearranged[0])
        return total+cycle
            
