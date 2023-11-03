class Solution:

	def checkTriplet(self,arr, n):
    	# code here
    	arr_set = set([x * x for x in arr])

        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the square of the sum of elements at indices i and j
                sum_of_squares = arr[i] * arr[i] + arr[j] * arr[j]

                # Check if the square of the sum is in the set
                if sum_of_squares in arr_set:
                    return True

        return False
