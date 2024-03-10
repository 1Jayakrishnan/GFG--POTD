class Solution:
	def removeDuplicates(self,str):
	    # code here
	    seen = set()
        result = []

        for char in str:
            if char not in seen:
                seen.add(char)
                result.append(char)

        return ''.join(result)
