class Solution:
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        s1_list = list(s1)
        sorted_s1 = sorted(s1_list)
        
        s2_list = list(s2)
        sorted_s2 = sorted(s2_list)
        
        s1 = "".join(sorted_s1)
        s2 = "".join(sorted_s2)
        
        if s1 == s2:
            return 1
        else:
            return 0
