class Solution:
    def gameOfXor(self, N , A):
        # code here 
        if N % 2 == 0:
            return 0

        XOR = 0
        for i in range(0, N, 2):
            XOR ^= A[i]
        
        return XOR
