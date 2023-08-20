class Solution:

	def count(self,arr, n, x):
		# code here
        self.x = x
        self.n = n
        self.arr = arr
        count=0
        for i in range(n):
            if arr[i] == x:
                count = count+1
                
        return count
