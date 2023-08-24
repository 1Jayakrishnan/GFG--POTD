class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        if s1[0] == '-':
            sign1 = -1
            s1 = s1[1:]
        else:
            sign1 = 1
            
        if s2[0] == '-':
            sign2 = -1
            s2 = s2[1:]
        else:
            sign2 = 1
            
        len1, len2 = len(s1), len(s2)
        result = [0] * (len1 + len2)
        
        for i in range(len1 - 1, -1, -1):
            carry = 0
            n1 = ord(s1[i]) - ord('0')
            
            for j in range(len2 - 1, -1, -1):
                n2 = ord(s2[j]) - ord('0')
                temp_sum = n1 * n2 + result[i + j + 1] + carry
                carry = temp_sum // 10
                result[i + j + 1] = temp_sum % 10
            
            result[i] += carry
        
        # Remove leading zeros from the result
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        
        if sign1 * sign2 == -1 and result != [0]:
            return '-' + ''.join(map(str, result))
        else:
            return ''.join(map(str, result))
