class Solution:
    def nQueen(self, n):
        def is_safe(queens, row, col):
            for r, c in enumerate(queens):
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def solve(queens, row):
            if row == n:
                results.append(queens[:])
                return
            for col in range(1, n + 1):
                if is_safe(queens, row, col):
                    solve(queens + [col], row + 1)

        results = []
        solve([], 0)
        return results
