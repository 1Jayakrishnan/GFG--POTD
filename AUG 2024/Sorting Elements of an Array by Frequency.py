from collections import Counter

class Solution:
    # Function to sort the array according to the frequency of elements.
    def sortByFreq(self, arr):
        # Counting the frequency of each element in the array
        freq = Counter(arr)
        
        # Sorting the array based on frequency (descending) and value (ascending)
        sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
        
        return sorted_arr
