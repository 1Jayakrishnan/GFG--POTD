class Solution:
    def asciirange(self, s):
        first_pos = {}
        last_pos = {}
        
        # Step 1: record first and last positions
        for i, ch in enumerate(s):
            if ch not in first_pos:
                first_pos[ch] = i
            last_pos[ch] = i  # always updates to latest occurrence

        result = []
        
        # Step 2: for each char with multiple occurrences, compute sum
        for ch in first_pos:
            start = first_pos[ch]
            end = last_pos[ch]
            if end > start + 1:  # there are elements strictly in between
                sum_ascii = sum(ord(s[i]) for i in range(start + 1, end))
                if sum_ascii > 0:
                    result.append(sum_ascii)

        return result
