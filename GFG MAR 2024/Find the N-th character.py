class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        length = len(s)

        for _ in range(r):
            new_s = ""
            for i in range(length):
                if s[i] == '0':
                    new_s += '01'
                else:
                    new_s += '10'
            
            s = new_s

        return s[n]
