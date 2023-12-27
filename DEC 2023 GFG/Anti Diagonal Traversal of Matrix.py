class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        def fill(i, j, mat, out):
            while i < len(mat) and j >= 0:
                out.append(mat[i][j])
                i += 1
                j -= 1

        out = []
        n = len(matrix)

        for j in range(n):
            fill(0, j, matrix, out)

        for i in range(1, n):
            fill(i, n - 1, matrix, out)

        return out
