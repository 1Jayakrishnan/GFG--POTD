class Solution:
    def findSpiral(self, root):
        if not root:
            return []

        result = []
        s1 = [root]   # Stack for levels to be printed right to left (even levels)
        s2 = []       # Stack for levels to be printed left to right (odd levels)

        while s1 or s2:
            # Process current level from s1 (right to left)
            while s1:
                node = s1.pop()
                result.append(node.data)

                # Right child first, then left child
                if node.right:
                    s2.append(node.right)
                if node.left:
                    s2.append(node.left)

            # Process current level from s2 (left to right)
            while s2:
                node = s2.pop()
                result.append(node.data)

                # Left child first, then right child
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)

        return result
