class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        if not root:
            return None

        # Helper function for in-order traversal and CDLL creation
        def convertToCDLL(node):
            nonlocal head, prev

            if not node:
                return

            # Recursively convert the left subtree
            convertToCDLL(node.left)

            # If this is the first node encountered, set it as the head
            if not head:
                head = node
            else:
                # Connect the previous node with the current node
                prev.right = node
                node.left = prev

            # Update the previous node to the current node
            prev = node

            # Recursively convert the right subtree
            convertToCDLL(node.right)

        # Initialize head and prev pointers
        head = None
        prev = None

        # Perform in-order traversal to convert to CDLL
        convertToCDLL(root)

        # Connect the head and tail of the CDLL
        if head and prev:
            head.left = prev
            prev.right = head

        return head
