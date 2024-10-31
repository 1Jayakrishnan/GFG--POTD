class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        #code here
        new_node = Node(x)
        
        # Case 1: Insert at the beginning if list is empty or x should be the new head
        if head is None or x <= head.data:
            new_node.next = head
            if head:
                head.prev = new_node
            return new_node  # New node is the new head of the list

        # Case 2: Traverse the list to find the correct position to insert x
        current = head
        while current.next and current.next.data < x:
            current = current.next

        # Insert new_node after the current node
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

        return head  # Head remains the same
