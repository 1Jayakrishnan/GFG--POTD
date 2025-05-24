class Solution:
    def sumSubstrings(self,s):
        # code here
        # x = '421'
        l=len(s)
        
        left = 0
        right = 0
        num = []
        while right < l:
            num.append(s[left:right+1])
            right += 1 
            if right == l:
                left += 1
                right = left
              
        int_num = list(map(int, num))  
        summ = sum(int_num)
        
        return summ
