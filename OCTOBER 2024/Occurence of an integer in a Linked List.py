class Solution:
    def count(self, head, key):
        # Code here
        ct = 0
        while head!=None:
            if head.data == key:
                ct += 1
            head = head.next
            
        return ct
