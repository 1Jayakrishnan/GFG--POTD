class Solution:
    def findFirstNode(self, head):
        #code here
        slow = head
        fast = head

        # Detect if a loop exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Loop detected
                break
        else:
            return None  # No loop found

        # Reset one pointer to the head
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # The meeting point is the first node of the loop
        return slow
