class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])
        
        top = 0
        bottom = row
        right = col
        left = 0 
        n = row * col 
        ct_num = 0
        
        output = []
        
        while ct_num < n:
            if ct_num < n:
                #top from left to right 
                for j in range(left, right):
                    output.append(mat[top][j])
                    ct_num += 1
                top += 1 
            
            if ct_num < n:    
                #right - up to down
                for i in range(top, bottom):
                    output.append(mat[i][right-1])
                    ct_num += 1
                right -= 1 
                
            if ct_num < n:
                #bottom - from left to right
                for j in range(right-1, left-1, -1):
                    output.append(mat[bottom-1][j])
                    ct_num += 1
                bottom -= 1 
            
            if ct_num < n:    
                #left - from down to up 
                for i in range(bottom-1, top-1, -1):
                    output.append(mat[i][left])
                    ct_num += 1
                left += 1 
                
        return output
