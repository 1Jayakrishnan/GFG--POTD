class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

class Solution:
    # Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        if not head:
            return None
        
        # Step 1: Create interleaved cloned nodes.
        curr = head
        while curr:
            new_node = Node(curr.data)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Set the random pointers of the newly created nodes.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next  # Move to the next original node.

        # Step 3: Separate the original and copied linked lists.
        original = head
        copy = head.next
        copy_head = copy  # Head of the copied list.
        
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        
        return copy_head
