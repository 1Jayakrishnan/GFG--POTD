class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, Key):
        # code here
        if root is None:
            return Node(Key)

        # Compare the key with the root's value.
        if Key < root.data:
            # Recursively insert into the left subtree.
            root.left = self.insert(root.left, Key)
        elif Key > root.data:
            # Recursively insert into the right subtree.
            root.right = self.insert(root.right, Key)

        # If key is equal to the root's value, no change needed.
        return root
