class Node: 
   
# Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None

class Solution:
    def deleteAlt(self, head):
        # code here
        if head is None or head.next is None:
            return head
        
        current = head
        
        while current and current.next:
            current.next = current.next.next
            
            current = current.next
            
        return head
