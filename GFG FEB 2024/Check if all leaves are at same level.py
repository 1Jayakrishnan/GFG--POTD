class Solution:
    def check(self, root):
        if not root:
            return True  # An empty tree is considered to have leaf nodes at the same level

        queue = [(root, 0)]  # Using a queue for level order traversal with level information
        leaf_level = None

        while queue:
            node, level = queue.pop(0)

            # Check if the current node is a leaf node
            if not node.left and not node.right:
                if leaf_level is None:
                    leaf_level = level
                elif level != leaf_level:
                    return False  # Leaf nodes are not at the same level

            # Enqueue left and right children with updated level information
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return True  # All leaf nodes are at the same level
