class Solution:
    # Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self, a, n):
        if n == 1:
            return 0

        ans = -1
        lmin = [0] * n
        rmax = [0] * n

        lmin[0] = a[0]
        for i in range(1, n):
            lmin[i] = min(lmin[i - 1], a[i])

        rmax[n - 1] = a[n - 1]
        for j in range(n - 2, -1, -1):
            rmax[j] = max(rmax[j + 1], a[j])

        i, j = 0, 0
        while i < n and j < n:
            if lmin[i] <= rmax[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans
