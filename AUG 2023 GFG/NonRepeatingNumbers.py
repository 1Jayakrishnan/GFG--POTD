class Solution:
	def singleNumber(self, nums):
		# Code here
        self.nums = nums
        xorAll = 0

        # Calculate XOR of all elements in the array
        for num in nums:
            xorAll ^= num
    
        # Find the rightmost set bit position
        rightmostSetBit = xorAll & -xorAll
    
        num1 = 0
        num2 = 0
    
        # Divide the elements into two groups based on the rightmost set bit
        for num in nums:
            if num & rightmostSetBit:
                num1 ^= num
            else:
                num2 ^= num
    
        # Return the distinct numbers in increasing order
        return [min(num1, num2), max(num1, num2)]
