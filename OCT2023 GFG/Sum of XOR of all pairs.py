class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        total_xor_sum = 0
        
        for i in range(32):  # Assuming 32-bit integers
            # Count the number of elements with i-th bit set
            count_on = 0
            for num in arr:
                if (num & (1 << i)) != 0:
                    count_on += 1
            
            # Count the number of elements with i-th bit not set
            count_off = n - count_on
            
            # For each bit, there will be count_on * count_off pairs that contribute 2^i to the sum
            xor_sum_bit = (count_on * count_off) * (1 << i)
            
            total_xor_sum += xor_sum_bit
        
        return total_xor_sum
