class Solution{
  public:
    // Return True if the given trees are isomotphic. Else return False.
    bool isIsomorphic(Node *root1,Node *root2)
    {
    //add code here.
       if (!root1 && !root2) {
        return true;
    }

    // If one tree is empty and the other is not, they are not isomorphic
    if ((!root1 && root2) || (root1 && !root2)) {
        return false;
    }

    // Check if the current nodes have the same value
    if (root1->data != root2->data) {
        return false;
    }

    // Check both subtrees:
    // 1. Without flipping
    // 2. With flipping (swap left and right)
    return (isIsomorphic(root1->left, root2->left) && isIsomorphic(root1->right, root2->right)) ||
           (isIsomorphic(root1->left, root2->right) && isIsomorphic(root1->right, root2->left));
    }
};
