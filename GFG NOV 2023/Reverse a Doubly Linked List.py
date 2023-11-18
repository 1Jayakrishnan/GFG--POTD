class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        current = head
        prev_node = None

        # Iterate through the list and reverse the pointers
        while current is not None:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node

            # Move to the next node
            prev_node = current
            current = next_node

        # The new head is the last node (prev_node after the loop)
        head = prev_node

        return head
