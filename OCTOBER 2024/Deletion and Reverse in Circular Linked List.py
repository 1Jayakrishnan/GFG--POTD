class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        # If the list is empty
        if not head:
            return None
        
        # Handle the case when the key is in the head node
        curr = head
        prev = None
        
        # If the node to be deleted is the head
        if head.data == key:
            # If there is only one node
            if head.next == head:
                return None
            
            # Find the last node (to maintain the circular nature)
            while curr.next != head:
                curr = curr.next
            
            # Update the head and point the last node to the new head
            curr.next = head.next
            head = head.next
            return head
        
        # Traverse the list to find the node with the given key
        curr = head
        while curr.next != head and curr.next.data != key:
            curr = curr.next
        
        # If the node is found, delete it
        if curr.next.data == key:
            curr.next = curr.next.next
        
        return head
    
    # Function to reverse a circular linked list
    def reverse(self, head):
        if not head or head.next == head:
            return head
        
        prev = None
        curr = head
        next_node = None
        last = head
        
        # Traverse the list to reverse the pointers
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == head:
                break
        
        # Complete the reverse by pointing head's next to prev
        last.next = prev
        return prev
