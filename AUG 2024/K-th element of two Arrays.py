class Solution:
    def kthElement(self, k, arr1, arr2):
        
        #combine two lists
        arr1.extend(arr2)
         
        #sort the arr1
        arr1.sort()
        
        return arr1[k-1]
        
