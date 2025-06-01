class Solution:
    def countPairs(self, mat1, mat2, x):
        freq = {}
        
        # Flatten mat2 into a frequency map
        for row in mat2:
            for num in row:
                freq[num] = freq.get(num, 0) + 1
        
        count = 0
        # Check in mat1
        for row in mat1:
            for num in row:
                complement = x - num
                if complement in freq:
                    count += freq[complement]
        
        return count
