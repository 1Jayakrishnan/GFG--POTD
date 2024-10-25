class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        left, right = 0, len(arr)-1
        new = []
        
        while left <= right:
            new.append(arr[right])
            right -= 1
            
            if left < right:
                new.append(arr[left])
                left += 1
            
        return new
