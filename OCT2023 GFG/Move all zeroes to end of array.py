class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	left = 0
        right = 0

        # Traverse the array
        while right < n:
            # If the current element is non-zero, swap it with the left pointer
            if arr[right] != 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
            right += 1
