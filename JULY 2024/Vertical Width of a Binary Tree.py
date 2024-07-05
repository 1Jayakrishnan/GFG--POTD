def verticalWidth(root):
    if not root: return 0
    l, r = float('inf'), float('-inf')
    def dfs(node, skew):
        nonlocal l, r
        if not node:
            return None
        if node.left:
            dfs(node.left, skew-1)
        l, r = min(l, skew), max(r, skew)
        if node.right:
            dfs(node.right, skew+1)
    dfs(root, 0)
    return r - l + 1
