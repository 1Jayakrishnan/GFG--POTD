class Solution:
    def inOrderTraversal(self, root, result):
        if root:
            self.inOrderTraversal(root.left, result)
            result.append(root.data)
            self.inOrderTraversal(root.right, result)
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        # code here
        result1, result2 = [], []
        
        # Perform in-order traversal on the first BST and store the elements in result1.
        self.inOrderTraversal(root1, result1)
        
        # Perform in-order traversal on the second BST and store the elements in result2.
        self.inOrderTraversal(root2, result2)
        
        # Initialize pointers for both lists.
        i, j = 0, 0
        common_elements = []

        # Compare the elements in the two lists while advancing the pointers.
        while i < len(result1) and j < len(result2):
            if result1[i] == result2[j]:
                common_elements.append(result1[i])
                i += 1
                j += 1
            elif result1[i] < result2[j]:
                i += 1
            else:
                j += 1
        
        return common_elements
