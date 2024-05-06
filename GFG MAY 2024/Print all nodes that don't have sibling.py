def noSibling(root):
    result = []
    def dfs(node):
        if not node:
            return
        if (node.left and not node.right):
            result.append(node.left.data)
        elif (node.right and not node.left):
            result.append(node.right.data)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return sorted(result) if result else [-1]
