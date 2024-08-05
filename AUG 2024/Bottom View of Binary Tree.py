from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        # Dictionary to store the bottom view of the tree
        bottom_view = {}
        
        # Queue for BFS traversal
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # Update the bottom view dictionary
            bottom_view[hd] = node.data
            
            # Add left and right children to the queue with updated horizontal distance
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Sort the horizontal distances and prepare the result
        sorted_distances = sorted(bottom_view.keys())
        result = [bottom_view[hd] for hd in sorted_distances]
        
        return result
