class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        # contrain is that there is atleast 1 node, but k can be 0 
        if k == 0:
            return head
        # get the length of the linked list to handle large k using k modulo length
        curr = head
        l = 1
        while curr.next is not None:
            curr = curr.next
            l += 1
        k %= l
        # if k is multiple of length, then no change in the linked list
        if k == 0:
            return head
        # make the current linkedlist circular
        curr.next = head
        # Traverse the linked list to find the kth node
        curr = head
        for _ in range(1, k):
            curr = curr.next
        # Update the (k + 1)th node as the new head
        head = curr.next
        # Break the loop by updating the next pointer of kth node
        curr.next = None
        return head
