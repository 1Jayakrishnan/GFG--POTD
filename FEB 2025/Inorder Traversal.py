class Solution:
    def inOrder(self, root):
        stack = []
        def push_left(n):
            nonlocal stack
            while n:
                stack.append(n)
                n = n.left
                
        push_left(root)
        
        ans = []
        while stack:
            root = stack.pop()
            ans.append(root.data)
            push_left(root.right)
        return ans
