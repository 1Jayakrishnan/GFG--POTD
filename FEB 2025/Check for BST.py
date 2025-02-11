
class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def helper(node, min_val, max_val):
            if node is None:
                return True
            # Check if current node's value violates the BST property.
            if not (min_val < node.data < max_val):
                return False
            # Recursively check left and right subtrees with updated ranges.
            return helper(node.left, min_val, node.data) and helper(node.right, node.data, max_val)
        
        # Initially, the allowed range is (-infinity, infinity).
        return helper(root, float('-inf'), float('inf'))
