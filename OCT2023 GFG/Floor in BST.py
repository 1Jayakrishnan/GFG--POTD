if not root:
            return -1  # The tree is empty, so no floor value is found.

        # Initialize variables to keep track of the current floor value and the current node.
        floor_value = -1
        current_node = root

        while current_node:
            if current_node.data == x:
                return x  # The current node value is equal to x, so the floor value is x.
            elif current_node.data < x:
                floor_value = current_node.data  # Update floor_value if the current node value is less than x.
                current_node = current_node.right  # Move to the right subtree to find a potentially larger floor value.
            else:
                current_node = current_node.left  # Move to the left subtree to find a smaller value.

        return floor_value  # Return the final floor value found during the traversal.
