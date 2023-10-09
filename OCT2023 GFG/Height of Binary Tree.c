int max(int a, int b) {
    return (a > b) ? a : b;
}

//Function to find the height of a binary tree.
int height(struct Node* node)
{
    //code here
    if (node == NULL) {
        return 0;
    } else {
        int leftHeight = height(node->left);
        int rightHeight = height(node->right);

        return 1 + max(leftHeight, rightHeight);
    }
}
