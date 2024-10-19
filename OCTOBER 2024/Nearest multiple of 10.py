class Solution:
    def roundToNearest (self, string) : 
        #Complete the function
        ans = ""
        n = len(string)
        
        if string[n-1] <= '5':
            ans = string[:-1] + '0'
        else:
            i = n - 1;
            ans = '0'
            carry = 1
            i -= 1
            
            while i >= 0:
                if string[i] == '9' and carry:
                    ans = '0' + ans
                    carry = 1
                else:
                    ans = str(int(string[i]) + carry) + ans
                    carry = 0
                
                i -= 1
            
            if carry:
                ans = '1' + ans
        
        return ans
