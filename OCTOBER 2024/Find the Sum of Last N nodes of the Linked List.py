# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        count = 0
        curr = head
        while head!=None:
            count += 1
            head = head.next
        
        fn = count - n
        
        total = 0
        ct = 0
        while curr!=None:
            ct += 1
            if ct > fn:
                total += curr.data
                
            curr = curr.next
            
        return total
       
