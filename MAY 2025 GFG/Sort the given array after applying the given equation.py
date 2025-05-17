class Solution:
	def sortArray(self, arr, A, B, C):
		# Code here
		newarray = []
		
	#	equation = A(x**2) + B(x) + C
	    
		
		for num in arr:
		    ans = A*(num**2) + B*(num) + C
		    #print(ans)
		    
		    newarray.append(ans)
		    
	    newarray.sort()
		
		return newarray
