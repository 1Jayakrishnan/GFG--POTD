class Solution:
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        # Create a dictionary to store the cumulative sum and its frequency
        cumsum_freq = {0: 1} # Initialize with 0:1 as a base case
        cumsum = 0
        count = 0

        for num in arr:
            # Update the cumulative sum
            cumsum += num

            # Check if the current cumulative sum minus the target is present in the dictionary
            if cumsum - tar in cumsum_freq:
                count += cumsum_freq[cumsum - tar]

            # Update the frequency of the current cumulative sum in the dictionary
            if cumsum in cumsum_freq:
                cumsum_freq[cumsum] += 1
            else:
                cumsum_freq[cumsum] = 1

        return count
