#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        current = head
        length = 0
        while current != None:
            length += 1
            current = current.next
        
        return length
            
