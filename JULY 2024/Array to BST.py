class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        def convertListToBST(left, right):
            if left > right:
                return None
            # Choose the middle element to maintain balance
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            # Recursively construct the left and right subtrees
            node.left = convertListToBST(left, mid - 1)
            node.right = convertListToBST(mid + 1, right)
            
            return node
        return convertListToBST(0, len(nums) - 1)
