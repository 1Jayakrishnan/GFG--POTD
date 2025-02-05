class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Base case: if the node is None, simply return None.
        if root is None:
            return None

        # Recursively convert the left and right subtrees.
        left_mirror = self.mirror(root.left)
        right_mirror = self.mirror(root.right)

        # Swap the left and right children.
        root.left, root.right = right_mirror, left_mirror

        return root
