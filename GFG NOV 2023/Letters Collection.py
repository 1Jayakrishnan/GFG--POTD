class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        out = []

        for k in range(q):
            sum = 0
            hop = queries[k][0]
            x = queries[k][1]
            y = queries[k][2]

            for i in range(x - hop, x + hop + 1):
                if 0 <= i < n:
                    if y - hop >= 0:
                        sum += mat[i][y - hop]
                    if y + hop < m:
                        sum += mat[i][y + hop]

            for i in range(y - hop + 1, y + hop):
                if 0 <= i < m:
                    if x - hop >= 0:
                        sum += mat[x - hop][i]
                    if x + hop < n:
                        sum += mat[x + hop][i]

            out.append(sum)

        return out
