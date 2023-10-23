class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		max_sum = [0] * n

        # Initialize max_sum array with values from Arr
        for i in range(n):
            max_sum[i] = Arr[i]

        # Iterate through the array to find the maximum sum increasing subsequence
        for i in range(1, n):
            for j in range(i):
                if Arr[i] > Arr[j] and max_sum[i] < max_sum[j] + Arr[i]:
                    max_sum[i] = max_sum[j] + Arr[i]

        # Find the maximum value in max_sum
        max_sequence_sum = max(max_sum)

        return max_sequence_sum
