class Solution {
    // Function to check whether all nodes of a tree have the value
    // equal to the sum of their child nodes.
    public static int isSumProperty(Node root) {
        // Base case: If the node is NULL, it follows the property.
        if (root == null) {
            return 1;
        }

        // If the node is a leaf, return 1.
        if (root.left == null && root.right == null) {
            return 1;
        }

        int leftSum = (root.left != null) ? root.left.data : 0;
        int rightSum = (root.right != null) ? root.right.data : 0;

        // Check if the current node's value is equal to the sum of its children.
        if (root.data == leftSum + rightSum &&
            isSumProperty(root.left) == 1 && isSumProperty(root.right) == 1) {
            return 1;
        } else {
            return 0;
        }
    }
}
