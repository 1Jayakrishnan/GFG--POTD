class Solution:
    def binaryNextNumber(self, s: str) -> str:
        # Convert the binary string to an integer
        num = int(s, 2)
        
        # Increment the integer by 1
        num += 1
        
        # Convert the incremented integer back to a binary string
        next_binary = bin(num)
        
        # Remove the '0b' prefix
        next_binary = next_binary[2:]
        
        return next_binary
