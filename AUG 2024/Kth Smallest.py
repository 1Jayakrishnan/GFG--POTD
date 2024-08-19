class Solution:

    def kthSmallest(self, arr,k):
        
        max_num = max(arr)
        
        count = [0] * (max_num + 1)
        
        for num in arr:
            count[num] = 1
        #print(count)
        ct = 0 
        for i in range(max_num+1):
            ct = ct + count[i]
            
            if ct == k:
                return i
