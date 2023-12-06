class Solution:    
    def countX(self,L,R,X):
        #code here
        count = 0

        # Iterate through the range (L + 1, R) excluding L and R
        for num in range(L + 1, R):
            # Count occurrences of X in each number
            count += str(num).count(str(X))

        return count
