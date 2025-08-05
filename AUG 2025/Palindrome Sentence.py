class Solution:
	def isPalinSent(self, s):
		# code here
		ss = ''
		for char in s:
		    if char.isalnum():
		        if char.isupper():
		            ss += char.lower()
		        else:
		            ss += char
		            
		return ss == ss[::-1]
                    
