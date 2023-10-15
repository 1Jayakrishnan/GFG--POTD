class Solution {
public:
    // Helper function to convert the BST to a sorted list
    void inOrderTraversal(Node* root, vector<int>& sorted) {
        if (root) {
            inOrderTraversal(root->left, sorted);
            sorted.push_back(root->data);
            inOrderTraversal(root->right, sorted);
        }
    }

    // Helper function to build a balanced BST from a sorted list
    Node* sortedArrayToBST(vector<int>& sorted, int start, int end) {
        if (start > end) {
            return nullptr;
        }

        int mid = (start + end) / 2;
        Node* root = new Node(sorted[mid]);

        root->left = sortedArrayToBST(sorted, start, mid - 1);
        root->right = sortedArrayToBST(sorted, mid + 1, end);

        return root;
    }

    Node* buildBalancedTree(Node* root) {
        if (!root) {
            return nullptr;
        }

        vector<int> sorted;
        // Convert the BST to a sorted list
        inOrderTraversal(root, sorted);

        // Build a balanced BST from the sorted list
        return sortedArrayToBST(sorted, 0, sorted.size() - 1);
    }
};
