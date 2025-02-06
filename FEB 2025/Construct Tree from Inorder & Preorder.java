class Solution {
    // Function to build tree from inorder and preorder traversals.
    public static Node buildTree(int inorder[], int preorder[]) {
        // preIndex is used as a pointer to track the root in the preorder array.
        int[] preIndex = new int[1];  // Using an array to simulate pass-by-reference.
        preIndex[0] = 0;
        return buildTreeHelper(inorder, preorder, 0, inorder.length - 1, preIndex);
    }
    
    // Recursive helper function to build the tree.
    private static Node buildTreeHelper(int[] inorder, int[] preorder, int inStart, int inEnd, int[] preIndex) {
        // Base case: if there are no elements to construct the subtree.
        if (inStart > inEnd) {
            return null;
        }
        
        // The current root is the next element in preorder.
        Node root = new Node(preorder[preIndex[0]++]);
        
        // If this node has no children, return it.
        if (inStart == inEnd) {
            return root;
        }
        
        // Find the index of this node in the inorder array.
        int inIndex = findIndex(inorder, inStart, inEnd, root.data);
        
        // Recursively construct the left and right subtrees.
        root.left = buildTreeHelper(inorder, preorder, inStart, inIndex - 1, preIndex);
        root.right = buildTreeHelper(inorder, preorder, inIndex + 1, inEnd, preIndex);
        
        return root;
    }
    
    // Utility function to find the index of a given value in the inorder array.
    private static int findIndex(int[] inorder, int inStart, int inEnd, int value) {
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == value)
                return i;
        }
        return -1; // Should not occur if input is valid.
    }
}
