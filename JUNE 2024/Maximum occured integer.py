class Solution:
    def maxOccured(self, n, l, r, maxx):
        # Create the frequency array with an additional space
        freq = [0] * (maxx + 2)
        
        # Mark the start and end+1 of each range
        for i in range(n):
            freq[l[i]] += 1
            freq[r[i] + 1] -= 1
        
        # Compute the prefix sum to get the frequency of each integer
        max_count = 0
        max_occured = -1
        current_count = 0
        
        for i in range(maxx + 1):
            current_count += freq[i]
            if current_count > max_count:
                max_count = current_count
                max_occured = i
        
        return max_occured
