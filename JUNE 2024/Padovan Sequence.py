class Solution:
    def padovanSequence(self, n):
        # code here 
        MOD = 10**9 + 7
        
        # Base cases
        if n == 0 or n == 1 or n == 2:
            return 1
        
        # Initialize variables for P(0), P(1), and P(2)
        p0, p1, p2 = 1, 1, 1
        
        # Compute values from P(3) to P(n) using three variables
        for i in range(3, n + 1):
            current = (p0 + p1) % MOD
            p0, p1, p2 = p1, p2, current
        
        return p2
