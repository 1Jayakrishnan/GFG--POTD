class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        ct = 0
        freq = {}
        
        for num in arr:
            complement = target - num
            if complement in freq:
                ct += freq[complement]  # Count all occurrences of the complement
            freq[num] = freq.get(num, 0) + 1  # Update the frequency of the current number
                
        return ct
