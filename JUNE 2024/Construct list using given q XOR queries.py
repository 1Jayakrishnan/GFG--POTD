from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        # Initialize the list with a single value 0
        s = [0]
        # Variable to store cumulative XOR
        cumulative_xor = 0
        
        # Process each query
        for query in queries:
            if query[0] == 0:
                # Insert x into the list, adjusted for cumulative XOR
                x = query[1]
                s.append(x ^ cumulative_xor)
            elif query[0] == 1:
                # Update the cumulative XOR with x
                x = query[1]
                cumulative_xor ^= x
        
        # Apply the cumulative XOR to all elements before sorting
        s = [a ^ cumulative_xor for a in s]
        
        # Sort the list before returning
        s.sort()
        return s
