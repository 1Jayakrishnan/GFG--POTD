class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return -1
        
        # Recursively compute the height of the left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        # The height of the tree is the greater height of its two subtrees, plus one edge for the current node.
        return max(left_height, right_height) + 1
