class Solution:
	def canPair(self, nuns, k):
		# Code here
		if len(nums) % 2 != 0:
            return False
        
        # Create a dictionary to store the frequency of remainders
        remainder_count = {}
        
        # Count the frequency of each remainder when divided by k
        for num in nums:
            remainder = num % k
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        # Check special case for remainder 0
        if remainder_count.get(0, 0) % 2 != 0:
            return False
        
        # Check for each remainder i, if there is a remainder k - i present and with the same frequency
        for i in range(1, k // 2 + 1):
            if remainder_count.get(i, 0) != remainder_count.get(k - i, 0):
                return False
        
        return True
