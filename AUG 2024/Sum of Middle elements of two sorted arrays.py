class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        for num in arr2:
            arr1.append(num)
            
        arr1.sort()
        
        n = len(arr1)
        
        if n%2 == 0:
            return arr1[(n//2)-1] + arr1[n//2]
        else:
            return arr1[n//2]
