class Solution:    
    def pairWiseSwap(self, head):
        # code here
        prev = None
        curr = head

        # Traverse the list and swap nodes pairwise
        while curr and curr.next:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = curr

            # Update the previous pair's next pointer
            if prev:
                prev.next = next_node
            else:
                # Update the new head of the list
                head = next_node

            # Move pointers to the next pair
            prev = curr
            curr = curr.next

        return head
