class Solution:
	def sumBitDifferences(self,arr, n):
    	# code here
    	total_bit_diff = 0
        
        # Iterate through each bit position (32 bits for integers)
        for i in range(32):
            count_set_bits = 0
            
            # Count the number of set bits at the current position
            for j in range(n):
                if (arr[j] & (1 << i)) != 0:
                    count_set_bits += 1
            
            # Calculate bit differences for the current position and update total sum
            total_bit_diff += count_set_bits * (n - count_set_bits) * 2
        
        return total_bit_diff
