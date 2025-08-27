class Solution:
    def countTriangles(self, arr):
        arr.sort()
        n = len(arr)
        count = 0

        # Fix the largest side one by one
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    # All elements between i and j form valid pairs with arr[j]
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        
        return count
