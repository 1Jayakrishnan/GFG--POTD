class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Check if the difference is even
        if (sum_a - sum_b) % 2 != 0:
            return -1
        
        delta = (sum_a - sum_b) // 2
        
        # Create a set for fast lookups in array b
        set_b = set(b)
        
        # Check for each element in array a if there's a corresponding element in array b
        for x in a:
            y = x - delta
            if y in set_b:
                return 1
        
        return -1
