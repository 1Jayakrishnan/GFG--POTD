class Solution:
    def subarrayXor(self, arr, k):
        # Initialize variables
        count = 0
        prefix_xor = 0
        freq = {0: 1}  # To handle cases where subarray starts from index 0
        
        for num in arr:
            # Update the prefix XOR
            prefix_xor ^= num
            
            # Check if prefix_xor ^ k exists in freq
            xor_needed = prefix_xor ^ k
            if xor_needed in freq:
                count += freq[xor_needed]
            
            # Update the frequency map
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count
