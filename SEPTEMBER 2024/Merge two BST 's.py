class Solution:
    # Helper function to perform inorder traversal of BST
    def inorder(self, root, arr):
        if root is None:
            return
        
        # Traverse the left subtree
        self.inorder(root.left, arr)
        
        # Add root's data to the array
        arr.append(root.data)
        
        # Traverse the right subtree
        self.inorder(root.right, arr)
    
    # Function to merge two sorted arrays
    def mergeArrays(self, arr1, arr2):
        i, j = 0, 0
        merged = []
        
        # Merge both arrays
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        # If there are remaining elements in arr1
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        
        # If there are remaining elements in arr2
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
        
        return merged
    
    # Function to merge two BSTs
    def merge(self, root1, root2):
        # Perform inorder traversal of both BSTs to get sorted arrays
        arr1, arr2 = [], []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        
        # Merge the two sorted arrays
        merged_array = self.mergeArrays(arr1, arr2)
        
        # Return the merged array (sorted elements of the two BSTs)
        return merged_array
