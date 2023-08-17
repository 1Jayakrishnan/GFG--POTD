class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        maxm =  0
        self.n = n
        self.a = a
        n=len(a)
        # initialize LIS values for all indexes
        lst = [1 for s in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if (a[i] > a[j] and lst[i] < lst[j] + 1):
                    lst[i] = lst[j] + 1
        # Pick maximum of all LIS values
        for i in range(0, n):
            if maxm < lst[i]:
                maxm = lst[i]
       
        return maxm
