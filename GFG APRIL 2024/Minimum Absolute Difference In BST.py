class Solution:
    def absolute_diff(self,root):
        # Your code here
        temp = []
        def solve(root):
            if not root:
                return
            solve(root.left)
            temp.append(root.data)
            solve(root.right)
        solve(root)
        ans = float("inf")
        for i in range(1,len(temp)):
            ans = min(ans, abs(temp[i]-temp[i-1]))
        return ans
