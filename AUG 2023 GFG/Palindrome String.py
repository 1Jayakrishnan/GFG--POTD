class Solution:
	def isPalindrome(self, S):
		# code here
        S = S.lower()  # Convert the string to lowercase
        S = ''.join(filter(str.isalnum, S))  # Remove non-alphanumeric characters
        
        if S == S[::-1]:
            return 1
        else:
            return 0
            
