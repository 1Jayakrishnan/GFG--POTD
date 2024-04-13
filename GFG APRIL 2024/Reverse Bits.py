class Solution:
    def reversedBits(self, x):
        # code here 
        result = 0
        
        # Iterate through each bit of the number
        for _ in range(32):  # Assuming 32-bit integers
            # Extract the least significant bit (LSB) of x
            lsb = x & 1
            
            # Append the LSB to the result
            result = (result << 1) | lsb
            
            # Shift x to the right to process the next bit
            x >>= 1
        
        # Return the result
        return result
