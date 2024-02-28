class Solution:
    def DivisibleByEight(self,s):
        #code here
        n = len(s)
        last_three_digits = int(s[max(n - 3, 0):])
        return 1 if last_three_digits % 8 == 0 else -1
