class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        x = 0
        y = 0
        
        # Determine x and y
        for char, count in freq.items():
            position = ord(char) - ord('a') + 1  # Get the position in the alphabet (1-based index)
            if position % 2 == 0:  # Even position in the alphabet
                if count % 2 == 0:  # Even frequency
                    x += 1
            else:  # Odd position in the alphabet
                if count % 2 == 1:  # Odd frequency
                    y += 1

        # Determine if the sum of x and y is even or odd
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
