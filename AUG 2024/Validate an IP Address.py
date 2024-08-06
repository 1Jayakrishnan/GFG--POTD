#User function Template for python3
class Solution:
    def isValid(self, ip_address):
        #code here
        ip_list = ip_address.split(".")
        
        if len(ip_list) != 4:
            return False
        
        for num in ip_list:

            if not num.isdigit() or (num != '0' and num[0] == '0'):
                return False
            
            num = int(num)
            if not (0 <= num <= 255):
                return False
    
        return True

