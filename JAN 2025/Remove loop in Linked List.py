class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return

        # Step 1: Detect if a loop exists using Floyd's Cycle Detection Algorithm
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Loop detected
                break
        else:
            return  # No loop detected, return as it is

        # Step 2: Find the start of the loop
        slow = head
        if slow == fast:  # Special case where the loop starts at the head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # Step 3: Remove the loop
        fast.next = None
