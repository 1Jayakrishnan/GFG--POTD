class Solution:
    def minRow(self,n,m,a):
        #code here
        #count the number of rows 1's in each row
        #store them in a list
        #find the minimum of the list and return its index+1
        count = [0] * n
        for i in range(n):
            for j in range(m):
                if a[i][j]==1:
                    count[i]+=1
        return(count.index(min(count)))+1
