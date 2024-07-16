#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
		c=0
		for i in range(len(s)):
		    if ch == s[i]:
		        c += 1
		        if c == count:
		            break
		        
	    if ((i+1) == len(s)):
	        return ""
	    else:
	        return s[i+1:]
