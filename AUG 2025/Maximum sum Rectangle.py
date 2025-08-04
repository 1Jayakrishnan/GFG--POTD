class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        max_sum = float('-inf')

        # Iterate over all pairs of columns
        for left in range(m):
            # Initialize a temporary row sum array
            temp = [0] * n
            for right in range(left, m):
                # Sum elements between left and right for each row
                for row in range(n):
                    temp[row] += mat[row][right]

                # Apply Kadane's algorithm to temp
                curr_sum = temp[0]
                max_ending_here = temp[0]
                for i in range(1, n):
                    max_ending_here = max(temp[i], max_ending_here + temp[i])
                    curr_sum = max(curr_sum, max_ending_here)

                # Update overall max sum
                max_sum = max(max_sum, curr_sum)

        return max_sum
