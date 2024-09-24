class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        from collections import defaultdict
        
        p_count = defaultdict(int)
        for char in p:
            p_count[char] += 1
        
        # Number of unique characters we need to match
        required = len(p_count)
        
        # Dictionary to store the frequency of characters in the current window
        window_count = defaultdict(int)
        
        # Two pointers to form a sliding window
        l, r = 0, 0
        
        # Number of unique characters in the current window that match the frequency in p_count
        formed = 0
        
        # Variables to store the answer (length of the window and start index)
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add the character on the right to the window
            char = s[r]
            window_count[char] += 1
            
            # If the frequency of the current character matches its required frequency in p_count
            if char in p_count and window_count[char] == p_count[char]:
                formed += 1
            
            # Try to contract the window from the left as long as it's valid (i.e., all characters are matched)
            while l <= r and formed == required:
                char = s[l]
                
                # Update the answer if this window is smaller than the previous best
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Remove the leftmost character from the window
                window_count[char] -= 1
                if char in p_count and window_count[char] < p_count[char]:
                    formed -= 1
                
                # Move the left pointer to contract the window
                l += 1
            
            # Move the right pointer to expand the window
            r += 1
        
        # If we found a valid window, return the smallest one; otherwise, return -1
        return s[ans[1]:ans[2] + 1] if ans[0] != float("inf") else "-1"
