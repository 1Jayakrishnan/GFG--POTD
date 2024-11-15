class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr_set = set(arr)
        
        arr_list = list(arr_set)
        
        arr_list.sort()
        
        if len(arr_list) <= 1:
            return -1
        else:
            return arr_list[-2]
