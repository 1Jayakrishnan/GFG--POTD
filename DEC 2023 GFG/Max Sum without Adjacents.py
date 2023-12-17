class Solution:
	def findMaxSum(self,arr, n):
		# code here
		if n == 0:
            return 0
        if n == 1:
            return arr[0]

        # Initialize two variables to store the maximum sum including and excluding the current element
        incl = arr[0]
        excl = 0

        # Iterate through the array starting from the second element
        for i in range(1, n):
            # Calculate the new incl and excl values considering the current element
            new_incl = excl + arr[i]
            new_excl = max(incl, excl)

            # Update incl and excl for the next iteration
            incl = new_incl
            excl = new_excl

        # Return the maximum of incl and excl as the result
        return max(incl, excl)
