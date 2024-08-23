from collections import deque

# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    # code here
    if not root:
        return []

    result = []
    queue = deque([root])
    
    while queue:
        # Number of nodes at the current level
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            
            # The first node in this level (i == 0) is part of the left view
            if i == 0:
                result.append(node.data)
                
            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result
