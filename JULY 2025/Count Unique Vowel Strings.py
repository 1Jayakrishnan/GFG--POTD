from math import factorial
from collections import Counter

class Solution:
    def vowelCount(self, s):
        vowels = 'aeiou'
        freq = Counter(ch for ch in s if ch in vowels)

        if not freq:
            return 0

        # Product of counts of distinct vowels
        product = 1
        for count in freq.values():
            product *= count
        
        # Multiply with factorial of number of unique vowels
        return product * factorial(len(freq))
