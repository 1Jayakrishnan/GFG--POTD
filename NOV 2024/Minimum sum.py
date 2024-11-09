from collections import deque
class Solution:
    def minSum(self, arr):
        n=len(arr)
        arr.sort(reverse=True)
        ans=deque()
        carry=0
        i=0
        while i<n and arr[i]!=0:
            val=arr[i]+carry
            if (i+1)<n:
                val+=arr[i+1]
            carry=val//10
            val=val%10
            ans.appendleft(str(val))
            i+=2
        if carry:
            ans.appendleft("1")
        return "".join(ans)
