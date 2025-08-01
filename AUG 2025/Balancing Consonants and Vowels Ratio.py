class Solution:
    def countBalanced(self, arr):
        vowels_set = set('aeiou')
        count_map = {0: 1}  # diff 0 seen once (empty prefix)
        diff = 0
        result = 0

        for s in arr:
            vowels = sum(1 for ch in s if ch in vowels_set)
            consonants = len(s) - vowels
            diff += (vowels - consonants)

            result += count_map.get(diff, 0)
            count_map[diff] = count_map.get(diff, 0) + 1

        return result
