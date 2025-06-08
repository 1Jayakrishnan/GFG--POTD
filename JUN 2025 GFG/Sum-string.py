class Solution:
    def isSumString(self, s):
        n = len(s)
        
        def isValid(s):
            return s == "0" or not s.startswith('0')

        def check(i, j, k):
            while k < n:
                num1 = int(s[i:j])
                num2 = int(s[j:k])
                sum_str = str(num1 + num2)
                next_k = k + len(sum_str)
                
                if next_k > n or s[k:next_k] != sum_str:
                    return False

                # move window forward
                i, j, k = j, k, next_k

            return True

        # Try all possible splits for the first and second numbers
        for i in range(1, n):
            for j in range(i+1, n):
                first = s[0:i]
                second = s[i:j]
                if isValid(first) and isValid(second):
                    if check(0, i, j):
                        return True
        return False
