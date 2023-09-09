class Solution:
    def kthLargest(self,root, k):
        #your code here
        self.kth_largest = None
        self.count = k
        self.reverse_inorder(root)
        return self.kth_largest

    def reverse_inorder(self, node):
        if not node or self.count == 0:
            return
        
        # Traverse the right subtree first
        self.reverse_inorder(node.right)
        
        # If count is 0, we've found the Kth largest element
        if self.count == 0:
            return
        
        # Decrement count and check if we've found the Kth largest element
        self.count -= 1
        if self.count == 0:
            self.kth_largest = node.data
            return
        
        # Traverse the left subtree
        self.reverse_inorder(node.left)
