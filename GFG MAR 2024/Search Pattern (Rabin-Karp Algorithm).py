class Solution:
    def search(self, pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        indexes = []

        # Iterate through the text string
        for i in range(text_length - pattern_length + 1):
            # Check if the substring of text matches the pattern
            if text[i:i+pattern_length] == pattern:
                indexes.append(i + 1)  # Adjusting the index to start from 1

        # Return the indexes
        return indexes
