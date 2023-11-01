class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        frequency = [0] * N

        # Count the frequencies of numbers in the original array.
        for num in arr:
            if 1 <= num <= N:
                frequency[num - 1] += 1

        # Modify the original array in-place with the frequencies.
        for i in range(N):
            arr[i] = frequency[i]
