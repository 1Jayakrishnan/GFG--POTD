class TreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # your code here
        if not parent:
            return None

        # Dictionary to hold created nodes
        nodes = {}
        
        # Creating all nodes
        for i in range(len(parent)):
            nodes[i] = TreeNode(i)
        
        root = None
        
        # Establishing parent-child relationships
        for i in range(len(parent)):
            if parent[i] == -1:
                root = nodes[i]
            else:
                pNode = nodes[parent[i]]
                if pNode.left is None:
                    pNode.left = nodes[i]
                else:
                    pNode.right = nodes[i]
        
        return root
    
