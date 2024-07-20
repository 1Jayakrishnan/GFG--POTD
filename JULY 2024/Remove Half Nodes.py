class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def RemoveHalfNodes(self, node):
        # Base case: If the node is None, return None
        if not node:
            return None
        
        # Recursively remove half nodes in left and right subtrees
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        # If this node is a half node with only left child, return left child
        if node.left and not node.right:
            return node.left
        
        # If this node is a half node with only right child, return right child
        if node.right and not node.left:
            return node.right
        
        # If this node is a full node or a leaf node, return the node itself
        return node

# Helper function to do inorder traversal
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []
