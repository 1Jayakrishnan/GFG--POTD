class Solution:    
    def ValidCorner(self, mat): 
        n = len(mat)
        m = len(mat[0])
        
        seen_pairs = set()

        for row in mat:
            ones = []
            # Find columns with 1s in the current row
            for j in range(m):
                if row[j] == 1:
                    ones.append(j)

            # Check all column pairs (i, j) with 1s
            for i in range(len(ones)):
                for j in range(i + 1, len(ones)):
                    col1 = ones[i]
                    col2 = ones[j]
                    # If this pair has been seen in previous rows, rectangle exists
                    if (col1, col2) in seen_pairs:
                        return True
                    seen_pairs.add((col1, col2))
        
        return False
