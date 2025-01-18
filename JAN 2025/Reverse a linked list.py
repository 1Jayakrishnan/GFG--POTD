class Solution:
    def reverseList(self, head):
        # Code here
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to the current node
            current = next_node       # Move current to the next node
        
        return prev  # prev will be the new head of the reversed list
