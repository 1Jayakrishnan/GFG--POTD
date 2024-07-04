class Solution:
    def removeAllDuplicates(self, head):
        #code here
        arr = []
        curr = head
        while curr!=None:
            arr.append(curr.data)
            curr = curr.next
            
        dp = [0]*(max(arr)+1)
        for i in range(len(arr)):
            dp[arr[i]]+=1
            
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if dp[curr.data] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
    
        return dummy.next
