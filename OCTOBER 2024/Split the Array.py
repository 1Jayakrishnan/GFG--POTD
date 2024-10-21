class Solution:
	def countgroup(self,arr): 
		#Complete the function
		MOD = 10 ** 9 + 7
		n = len(arr)
		total = 0
		for num in arr:
		    total ^= num
		    
		if total != 0:
		    return 0
		
		return n
