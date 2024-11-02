class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        for i in range(len(arr)):
            new = arr[i+1:i+k+1]
            if arr[i] in new:
                return 1
                
        return 0
