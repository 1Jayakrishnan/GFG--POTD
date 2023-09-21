class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        if n == 0:
            return 0
        if n == 1:
            return a[0]

        prev_max = a[0]
        curr_max = max(a[0], a[1])
        
        for i in range(2, n):
            
            new_max = max(curr_max, prev_max + a[i])
            prev_max = curr_max
            curr_max = new_max

        return curr_max
