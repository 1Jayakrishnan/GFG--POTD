class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        a = 0
        b = n - 1
        
        while a < b:
            if mat[a][b] == 1:
                a += 1 # a knows b, so a cannot be the celebrity
            else:
                b -= 1 # a does not know b, so b cannot be the celebrity
        # a is now the potential celebrity
        candidate = a
        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        
        return candidate
