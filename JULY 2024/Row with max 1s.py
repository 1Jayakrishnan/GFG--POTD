class Solution:
	def rowWithMax1s(self,arr):
		# code here
		count = []
		ct = 0
		for i in range(len(arr)):
		    for j in range(len(arr[0])):
		        if arr[i][j] == 1:
		            ct += 1
		    count.append(ct)
		    ct = 0
		    
		# Check if all elements are zero
        if all(element == 0 for row in arr for element in row):
            return -1
        else:
	        return count.index(max(count))
