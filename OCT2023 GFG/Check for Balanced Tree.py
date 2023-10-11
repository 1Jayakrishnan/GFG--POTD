class Solution:
    def isBalanced(self,root):
    
        #add code here
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            
            # If any subtree is not balanced, return -1
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            # Otherwise, return the height of the current node's subtree
            return max(left_height, right_height) + 1

        # Start the recursion from the root of the tree
        return height(root) != -1
