class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        l = 0
        temp = head
        while temp != None:
            l += 1
            temp = temp.next
          
        length = 1 
        while length != ((l//2)+1):
            length += 1
            head = head.next
            
        return head.data
        
