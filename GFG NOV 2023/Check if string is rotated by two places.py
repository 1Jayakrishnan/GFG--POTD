class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        if len(str1) != len(str2):
            return False

        # Concatenate the first two characters of 'a' at the end
        rotated_str1_1 = str1[2:] + str1[:2]
        # Concatenate the last two characters of 'a' at the beginning
        rotated_str1_2 = str1[-2:] + str1[:-2]

        # Check if either rotated string is equal to 'b'
        return str2 == rotated_str1_1 or str2 == rotated_str1_2
