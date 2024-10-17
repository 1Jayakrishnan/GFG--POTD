class Solution:
    def alternatingSplitList(self, head):
        # Edge case: if the list is empty, return two empty lists
        if not head:
            return [None, None]

        # Initialize pointers for two new lists: a and b
        a = None
        b = None
        a_tail = None
        b_tail = None

        # Initialize a flag to alternate between lists
        is_a_turn = True

        # Traverse the original list
        current = head
        while current:
            if is_a_turn:
                # Add the current node to list a
                if not a:
                    a = current
                    a_tail = current
                else:
                    a_tail.next = current
                    a_tail = a_tail.next
            else:
                # Add the current node to list b
                if not b:
                    b = current
                    b_tail = current
                else:
                    b_tail.next = current
                    b_tail = b_tail.next

            # Move to the next node in the original list
            current = current.next
            # Toggle the flag to alternate
            is_a_turn = not is_a_turn

        # Terminate both lists
        if a_tail:
            a_tail.next = None
        if b_tail:
            b_tail.next = None

        # Return the two sub-lists as an array
        return [a, b]
