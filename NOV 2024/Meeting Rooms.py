class Solution:
    def canAttend(self,arr):
        # Your Code Here
        
        #sort the meeting acording to the starting time
        arr.sort(key=lambda x: x[0])
        
        # Check for overlapping meetings
        for i in range(1, len(arr)):
            # If the current meeting starts before the previous one ends, return False
            if arr[i][0] < arr[i - 1][1]:
                return False
        
        # If no overlaps are found, return True
        return True
            
