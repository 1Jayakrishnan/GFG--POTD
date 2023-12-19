class Solution:
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        xor_result = m ^ n

        # If both numbers are the same, return -1.
        if xor_result == 0:
            return -1

        # Find the position of the rightmost set bit in the XOR result.
        position = 1
        while (xor_result & 1) == 0:
            xor_result >>= 1
            position += 1

        return position
