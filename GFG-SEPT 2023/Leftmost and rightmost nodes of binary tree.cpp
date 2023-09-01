void printCorner(Node *root)
{

// Your code goes here
    if (!root) {
        return;
    }

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size();
        Node* leftmost = nullptr;
        Node* rightmost = nullptr;

        for (int i = 0; i < levelSize; i++) {
            Node* node = q.front();
            q.pop();

            if (i == 0) {
                leftmost = node;
            }
            if (i == levelSize - 1) {
                rightmost = node;
            }

            if (node->left) {
                q.push(node->left);
            }
            if (node->right) {
                q.push(node->right);
            }
        }

        cout << leftmost->data << " ";

        // Print the rightmost node if it's different from the leftmost
        if (rightmost != leftmost) {
            cout << rightmost->data << " ";
        }
    } 

}
