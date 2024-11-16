class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	# Initialize a pointer for the position of the next non-zero element
        non_zero_index = 0

        # Traverse the array
        for i in range(len(arr)):
            # If the current element is non-zero, swap it with the element at non_zero_index
            if arr[i] != 0:
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                # Increment the non_zero_index
                non_zero_index += 1
    	        
    	    
