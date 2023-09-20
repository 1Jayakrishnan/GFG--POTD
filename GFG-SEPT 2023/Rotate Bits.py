class Solution:
    def rotate(self, N, D):
        # code here
        mask_16 = (1 << 16) - 1
        D = D % 16
        
        out = [0, 0]
        out[0] = (N << D | (N >> (16 - D))) & mask_16
        out[1] = (N >> D | (n << (16 - D))) & mask_16
        
        return out
