class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None



class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        n=len(mat)
        for i in range(0,n):
            for j in range(0,n):
                mat[i][j]=Node(mat[i][j])
                if j>0:
                    mat[i][j-1].right=mat[i][j]
                if i>0:
                    mat[i-1][j].down=mat[i][j]
        return mat[0][0]
