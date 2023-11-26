class Solution:
    def pattern(self, N):
        # code here
        if N <= 0:
            return [N]
        
        toggle = -5
        c = N
        out = []
        
        while True:
            out.append(c)
            c += toggle
            if c <= 0:
                toggle = -toggle
            
            if c == N:
                break
        
        out.append(N)
        return out
