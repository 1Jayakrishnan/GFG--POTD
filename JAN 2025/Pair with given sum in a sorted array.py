class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        # Inialize freqency map and counter
        freq = {}
        cnt = 0
        for ele in arr:
            # check if required number to add upto target is in frequency map  
            if target - ele in freq:
                # add the cummulative frequency, upto current step, of required number 
                cnt += freq[target - ele]
            # update cummulative frequency map
            if ele in freq:
                freq[ele] +=1
            else:
                freq[ele] =1
        return cnt
