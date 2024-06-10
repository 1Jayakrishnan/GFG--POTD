class Solution:

	def matchPairs(self, n, nuts, bolts):
        bolts.sort()
        nuts.sort()
        return nuts,bolts
