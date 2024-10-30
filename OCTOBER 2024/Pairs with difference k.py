class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
        count = 0
	    hashMap = {}
    	for i in arr:
    	    hashMap[i] = hashMap.get(i, 0) + 1
    	   
    	for number in arr:
    	    c = number + k
    	    if c in hashMap:
    	        count += hashMap[c]
    	return count
