class Solution:
    def mergeArrays(self, a, b):
        # code here
        n, m = len(a), len(b)
        i, j = n - 1, 0  # Start with the largest in `a` and smallest in `b`

        # Swap elements to maintain order
        while i >= 0 and j < m and a[i] > b[j]:
            a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1

        # Re-sort both arrays
        a.sort()
        b.sort()

        # Output the modified arrays
        return a, b
