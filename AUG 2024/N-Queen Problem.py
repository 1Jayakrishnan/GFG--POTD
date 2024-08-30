class Solution:
    def nQueen(self, n):
        # Helper function to check if it's safe to place a queen at board[row][col]
        def is_safe(row, col):
            # Check if there is a queen in the same row
            if rows[row] or hills[row - col] or dales[row + col]:
                return False
            return True
        
        # Backtracking function to place queens on the board
        def backtrack(col):
            for row in range(n):
                if is_safe(row, col):
                    # Place queen
                    rows[row] = 1
                    hills[row - col] = 1
                    dales[row + col] = 1
                    queen_positions[col] = row + 1

                    # If we placed all queens successfully
                    if col + 1 == n:
                        result.append(queen_positions[:])
                    else:
                        # Move to the next column
                        backtrack(col + 1)
                    
                    # Backtrack and remove the queen
                    rows[row] = 0
                    hills[row - col] = 0
                    dales[row + col] = 0

        result = []
        rows = [0] * n  # Keeps track of occupied rows
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals
        queen_positions = [0] * n  # To store the current placement of queens

        backtrack(0)
        return result
