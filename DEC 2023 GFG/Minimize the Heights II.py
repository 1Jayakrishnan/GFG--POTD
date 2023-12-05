class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        out = arr[n - 1] - arr[0]

        for i in range(n - 1):
            if arr[i + 1] - k >= 0:
                nax = max(arr[i] + k, arr[n - 1] - k)
                nin = min(arr[i + 1] - k, arr[0] + k)
                out = min(out, nax - nin)

        return out
