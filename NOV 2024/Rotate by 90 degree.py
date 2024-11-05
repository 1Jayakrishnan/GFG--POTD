def rotate(mat): 
    #code here
    n = len(mat)
     # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        mat[i].reverse()
