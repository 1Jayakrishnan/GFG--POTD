class Solution:
    def printArr(self, n, arr):
        # printing array elements with spaces
        print(*arr)

    def setToZero(self, n, arr):
        # setting all elements to zero
        for i in range(n):
            arr[i] = 0

    def xor1ToN(self, n, arr):
        # doing xor with indices
        for i in range(n):
            arr[i] ^= i
        
