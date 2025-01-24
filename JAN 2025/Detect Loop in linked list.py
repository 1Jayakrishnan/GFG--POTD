class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        s,f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
