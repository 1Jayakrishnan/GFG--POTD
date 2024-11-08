
class Solution:
    def minRepeats(self, s1, s2):
        # code here 
        rep = s1
        count = 1
        while len(s1)<len(s2):
            s1 += rep
            count += 1
            
        if s1.find(s2) != -1:
            return count
        else:
            s1 += rep
            count += 1
        
        if s1.find(s2)!=-1:
            return count
        else:
            return -1
