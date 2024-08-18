class Solution:
    def canSplit(self, arr):
        #code here
        total = 0
        for num in arr:
            total += num
            
        if (total % 2 != 0):
            return False
        
        s = 0
        for num in arr:
            s += num
            
            if s == total//2:
                return True
        
        return False
