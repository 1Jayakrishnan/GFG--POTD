class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        # Sorting based on end times
        # Pair each number with its index
        indexed_numbers = list(enumerate(end))
        # Sort the list based on the number values in-place
        indexed_numbers.sort(key=lambda x: x[1])
        # Extract sorted indices and values
        sorted_indices = [index for index, value in indexed_numbers]
        end = [value for index, value in indexed_numbers]
        # Rearranging the start list based on the indices
        start = [start[i] for i in sorted_indices]
        # Find the maximum number of non-overlapping meetings
        count = 1  # At least one meeting can be held
        prev_end_time = end[0]
        
        for i in range(1, n):
            if start[i] > prev_end_time:
                count += 1
                prev_end_time = end[i]
                
        return count
