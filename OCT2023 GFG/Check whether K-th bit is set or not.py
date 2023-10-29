class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        if (n >> k) & 1:
            return True
        else:
            return False
