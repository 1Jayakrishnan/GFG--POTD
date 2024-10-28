class Solution:
    def removeDuplicates(self, arr):
        # code here 
        new_arr = []
        for num in arr:
            if num not in new_arr:
                new_arr.append(num)
                
        return new_arr
