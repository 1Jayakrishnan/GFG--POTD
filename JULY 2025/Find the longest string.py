class Solution():
    def longestString(self, words):
        word_set = set(words)
        # Sort by descending length, then lexicographically
        words.sort(key=lambda x: (-len(x), x))

        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid:
                return word

        return ""
