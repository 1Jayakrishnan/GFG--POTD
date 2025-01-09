class Solution:
    def subarraySum(self, arr, target):
        # code here
        for i in range(len(arr)):
            j = i 
            s = 0
            while j < len(arr) and s <= target:
                s += arr[j]
                if s == target:
                    return [i+1, j+1]
                else:
                    j += 1 
        return [-1]
