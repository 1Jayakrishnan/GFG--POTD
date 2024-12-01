from collections import Counter
class Solution:
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # Dictionary to store frequency of each character
        # char_count = {}
        
        # # Traverse the string and count frequencies
        # for char in s:
        #     char_count[char] = char_count.get(char, 0) + 1
        
        # # Traverse the string again to find the first non-repeating character
        # for char in s:
        #     if char_count[char] == 1:
        #         return char
        
        # # If no non-repeating character found, return '$'
        # return '$'
        
        freq = Counter(s)
        #print(freq)
        for char in freq:
            if freq[char] == 1:
                return char
        
        return '$'
