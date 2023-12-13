class Solution:

	def countStrings(self,n):
    	# code here
    	# Initialize arrays to store counts
        ends_with_0 = [0] * (n + 1)
        ends_with_1 = [0] * (n + 1)

        # Base cases
        ends_with_0[1] = 1
        ends_with_1[1] = 1

        # Fill the arrays using dynamic programming
        for i in range(2, n + 1):
            ends_with_0[i] = (ends_with_0[i - 1] + ends_with_1[i - 1]) % (10**9 + 7)
            ends_with_1[i] = ends_with_0[i - 1]

        # Calculate the total count of binary strings of length N
        result = (ends_with_0[n] + ends_with_1[n]) % (10**9 + 7)
        return result
