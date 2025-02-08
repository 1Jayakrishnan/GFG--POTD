class Solution:
    def boundaryTraversal(self, root):
        # Code here
        if root is None:
            return []
        
        # Helper to check if a node is a leaf
        def isLeaf(node):
            return node.left is None and node.right is None
        
        result = []
        
        # Add root if it's not a leaf.
        if not isLeaf(root):
            result.append(root.data)
        
        # Add left boundary (excluding leaf nodes)
        cur = root.left
        while cur:
            if not isLeaf(cur):
                result.append(cur.data)
            # Prefer the left child; if not available, take the right child.
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        # Add all leaf nodes in left-to-right order.
        def addLeaves(node):
            if node is None:
                return
            if isLeaf(node):
                result.append(node.data)
            else:
                addLeaves(node.left)
                addLeaves(node.right)
        addLeaves(root)
        
        # Add right boundary (excluding leaf nodes) in reverse order.
        temp = []
        cur = root.right
        while cur:
            if not isLeaf(cur):
                temp.append(cur.data)
            # Prefer the right child; if not available, take the left child.
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        # Add the right boundary in reverse order.
        result.extend(temp[::-1])
        
        return result
