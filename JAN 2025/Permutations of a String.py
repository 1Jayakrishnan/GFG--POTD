from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Use a set to store unique permutations
        unique_permutations = set(permutations(s))
        # Convert tuples to strings and return as a list
        return [''.join(p) for p in unique_permutations]
