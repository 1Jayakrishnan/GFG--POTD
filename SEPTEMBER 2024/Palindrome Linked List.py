class Solution:
    # Helper function to reverse the linked list
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    #Function to check whether the list is palindrome.
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        second_half = self.reverseList(slow)
        
        # Step 3: Compare the first and second halves
        first_half = head
        second_half_copy = second_half # Save for restoring the list later (optional)
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        # Optional: Restore the list to its original form
        self.reverseList(second_half_copy)
        
        return True

# Helper class for ListNode (if needed)
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
