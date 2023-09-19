class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        position = 1  # Initialize the position to 1 (rightmost bit).
        
        # If n is 0, there is no set bit, so return 0.
        if n == 0:
            return 0

        # Iterate through the binary representation of n.
        while n > 0:
            # Check if the current bit is set (i.e., if it's 1).
            if n & 1:
                return position
            # If the current bit is not set, right-shift n and increment the position.
            n >>= 1
            position += 1

        # If there are no set bits, return 0.
        return 0
