class Solution:
    def solveSudoku(self, mat):
        row_used = [[False] * 10 for _ in range(9)]
        col_used = [[False] * 10 for _ in range(9)]
        box_used = [[False] * 10 for _ in range(9)]
        empty_cells = []

        # Preprocess the board and mark used numbers
        for r in range(9):
            for c in range(9):
                num = mat[r][c]
                if num:
                    row_used[r][num] = True
                    col_used[c][num] = True
                    box_used[(r // 3) * 3 + (c // 3)][num] = True
                else:
                    empty_cells.append((r, c))

        def solve(index):
            if index == len(empty_cells):
                return True  # Solved successfully

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for num in range(1, 10):
                if not row_used[r][num] and not col_used[c][num] and not box_used[box_idx][num]:
                    # Place number
                    mat[r][c] = num
                    row_used[r][num] = col_used[c][num] = box_used[box_idx][num] = True

                    if solve(index + 1):  # Recursive call
                        return True

                    # Backtrack
                    mat[r][c] = 0
                    row_used[r][num] = col_used[c][num] = box_used[box_idx][num] = False

            return False  # No solution

        solve(0)
