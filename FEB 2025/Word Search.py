class Solution:
    def isWordExist(self, mat, word):
        if not mat or not mat[0]:
            return False
        
        n = len(mat)
        m = len(mat[0])
        
        # Helper function for DFS search.
        def dfs(r, c, index):
            # If we've matched all characters in the word, return True.
            if index == len(word):
                return True
            
            # Check boundaries and if the current cell matches the word at index.
            if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] != word[index]:
                return False
            
            # Mark the current cell as visited by temporarily changing its value.
            temp = mat[r][c]
            mat[r][c] = '#'  # Using '#' as a marker to indicate this cell is used.
            
            # Explore all 4 possible directions: down, up, right, left.
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Restore the original value (backtrack).
            mat[r][c] = temp
            return found
        
        # Try starting DFS from each cell in the matrix.
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
