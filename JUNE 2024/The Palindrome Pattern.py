class Solution:
    def pattern (self, arr):
        # code here
        #check palindrome in row wise
        for i in range(len(arr)):
            row=""
            for j in range(len(arr[0])):
                row=row+str(arr[i][j])
            
            if row==row[::-1]:
                ans=str(i)+" R"
                return ans
        
        #check palindrome in row wise
        for i in range(len(arr)):
            col=""
            for j in range(len(arr[0])):
                col=col+str(arr[j][i])
            
            if col==col[::-1]:
                ans=str(i)+" C"
                return ans
        
        #if no palindrome found 
        return -1
