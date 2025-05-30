class Solution:
    def findMaxFork(self, root, k):
        res = -1  # If no value ≤ k exists, you can return -1 or some indicator
        while root:
            if root.data == k:
                return root.data  # Exact match found
            elif root.data < k:
                res = root.data  # Potential result, go right to find closer value
                root = root.right
            else:
                root = root.left  # Go left to find smaller values
        return res
