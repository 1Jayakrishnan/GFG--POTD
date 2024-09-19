class Solution:
    #Function to reverse words in a given string.
    def reverseWords(self,string):
        # code here 
        words = string.split(".")
        #print(words)
        rev_words = words[::-1]
        #print(rev_words)
        return ".".join(rev_words)
