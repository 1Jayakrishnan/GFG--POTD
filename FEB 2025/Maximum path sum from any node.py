class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        ans = float('-inf')
        def walk(n):
            nonlocal ans
            if not n:
                return 0
            
            left = walk(n.left)
            right = walk(n.right)
            ans = max(ans, left+n.data+right)
            return max(max(left, right)+n.data, 0)
        walk(root)
        return ans
