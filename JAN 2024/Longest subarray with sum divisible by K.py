class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
        remainder_dict = {0: -1}
        
        # Initialize variables to store the current prefix sum and the length of the longest subarray
        prefix_sum = 0
        max_length = 0

        for i in range(n):
            # Calculate the current prefix sum
            prefix_sum = (prefix_sum + arr[i]) % K
            
            # If the current remainder is already in the dictionary, update max_length
            if prefix_sum in remainder_dict:
                max_length = max(max_length, i - remainder_dict[prefix_sum])
            
            # If the current remainder is not in the dictionary, add it with its index
            if prefix_sum not in remainder_dict:
                remainder_dict[prefix_sum] = i

        return max_length
