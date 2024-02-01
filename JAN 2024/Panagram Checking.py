class Solution:
    # Function to check if a string is Pangram or not.
    def checkPangram(self, s):
        # Create a set to store unique characters in the string.
        char_set = set()

        # Traverse through each character in the string.
        for char in s:
            # Check if the character is an alphabet and convert it to lowercase.
            if char.isalpha():
                char_set.add(char.lower())

        # Check if the length of the set is equal to 26 (number of English alphabets).
        return len(char_set) == 26
