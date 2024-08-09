class Solution:
    def Maximize(self, a): 
        # Complete the function
        
        MOD = 10**9 + 7
        #sort array a
        a.sort()
        
        arr_sum = 0
        for i in range(len(a)):
            arr_sum += a[i] * i
            
        return arr_sum % MOD
