class Solution:
    def LCA(self, root, n1, n2):
        while root:
            # Compare the data of the nodes.
            if root.data > n1.data and root.data > n2.data:
                # Both nodes are in the left subtree.
                root = root.left
            elif root.data < n1.data and root.data < n2.data:
                # Both nodes are in the right subtree.
                root = root.right
            else:
                # We've found the split point.
                return root
        return None
    
