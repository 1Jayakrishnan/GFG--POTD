class Solution:
    def longestUniqueSubstr(self, s):
        if not s:
            return 0
        
        char_map = {}
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            if s[end] in char_map and char_map[s[end]] >= start:
                # Move the start pointer to exclude the repeated character
                start = char_map[s[end]] + 1
            
            # Update the character's last seen position
            char_map[s[end]] = end
            
            # Calculate the length of the current substring
            max_length = max(max_length, end - start + 1)
        
        return max_length
