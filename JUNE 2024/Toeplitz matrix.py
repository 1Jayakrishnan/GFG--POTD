def isToepliz(mat):
    #code here
    rows=len(mat)
    cols=len(mat[0])
    for i in range(1,rows):
        for j in range(1,cols):
            if mat[i][j] != mat[i-1][j-1]:
                return 0
                
    
    return 1
