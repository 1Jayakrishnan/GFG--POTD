class Solution:
    def swapNibbles (self, n):
        # code here 
        high_nibble = (n & 0xF0) >> 4
        # Extract the low nibble and shift it to the left
        low_nibble = (n & 0x0F) << 4
        # Combine the two nibbles
        return high_nibble | low_nibble
