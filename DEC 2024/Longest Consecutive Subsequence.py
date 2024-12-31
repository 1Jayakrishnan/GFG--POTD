class Solution:
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        num_set = set(arr)
        longest_streak = 0

        for num in num_set:
            # Start a new sequence only if `num - 1` is not in the set
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count the consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
                
