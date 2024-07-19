class Solution:
    def constructLowerArray(self, arr):
        def merge_sort(arr, indices, counts, left, right):
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, indices, counts, left, mid)
            merge_sort(arr, indices, counts, mid, right)
            merge(arr, indices, counts, left, mid, right)

        def merge(arr, indices, counts, left, mid, right):
            i, j = left, mid
            temp = []
            while i < mid and j < right:
                if arr[indices[i]] <= arr[indices[j]]:
                    temp.append(indices[i])
                    counts[indices[i]] += j - mid
                    i += 1
                else:
                    temp.append(indices[j])
                    j += 1
            while i < mid:
                temp.append(indices[i])
                counts[indices[i]] += j - mid
                i += 1
            while j < right:
                temp.append(indices[j])
                j += 1
            for k in range(left, right):
                indices[k] = temp[k - left]

        n = len(arr)
        counts = [0] * n
        indices = list(range(n))
        merge_sort(arr, indices, counts, 0, n)
        return counts
