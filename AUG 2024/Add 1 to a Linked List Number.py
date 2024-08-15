class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        # Convert linked list to integer
        num = 0
        current = head
        while current:
            num = num * 10 + current.data
            current = current.next
        
        # Add one to the number
        num += 1
        
        # Convert the number back to a linked list
        # Special case for num = 0
        if num == 0:
            return Node(0)
        
        # Create the linked list from the number
        dummy = Node(0)
        current = dummy
        # Convert number to linked list in reverse
        for digit in str(num):
            current.next = Node(int(digit))
            current = current.next
        
        # Return the new head
        return dummy.next
