class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMid(self, head):
        if not head or not head.next:
            return None  # No middle node to delete
        
        # Initialize slow and fast pointers
        slow = fast = head
        prev_slow = None  # Track previous of slow pointer
        
        # Move fast pointer to the end of the list and slow pointer will be at the middle node
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node (if there are two middle nodes, delete the second one)
        if prev_slow:
            prev_slow.next = slow.next
        else:
            head = slow.next
        
        return head

# Function to print the linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
