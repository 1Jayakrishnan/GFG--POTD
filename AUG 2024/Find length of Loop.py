class Solution:
    # Function to detect loop in the linked list and return its length
    def countNodesInLoop(self, head):
        if not head:
            return 0
        
        slow = fast = head
        
        # Step 1: Detect loop using Floyd’s cycle-finding algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast meet, there is a loop
            if slow == fast:
                # Step 2: Calculate the length of the loop
                return self.countLoopLength(slow)
        
        # If no loop is found
        return 0
    
    # Helper function to count the number of nodes in a loop
    def countLoopLength(self, node_in_loop):
        count = 1
        current = node_in_loop
        
        # Move through the loop until we reach the starting point again
        while current.next != node_in_loop:
            count += 1
            current = current.next
        
        return count

# Node class definition for a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Helper function to create a linked list with a loop for testing
def create_linked_list(arr, loop_pos):
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    loop_node = None
    
    for index in range(1, len(arr)):
        current.next = Node(arr[index])
        current = current.next
        if index == loop_pos:
            loop_node = current
    
    # If loop position is valid, create a loop
    if loop_node:
        current.next = loop_node
    
    return head
