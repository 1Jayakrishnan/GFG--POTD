class Solution:
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def sumOfLeafNodes(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            # Leaf node
            return root.data

        # Recursively calculate the sum for left and right subtrees
        left_sum = self.sumOfLeafNodes(root.left)
        right_sum = self.sumOfLeafNodes(root.right)

        return left_sum + right_sum
