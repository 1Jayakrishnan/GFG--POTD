class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        #if not arr:
        # return -1
        #find the shortest string element in the array and find Length
        prefix = min(arr) 
        min_len = len(prefix)
        
        for l in range(min_len,0,-1):
            if all(st[:l] == prefix[:l] for st in arr):
                return prefix[:l]
            
        return -1
