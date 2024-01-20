
class Solution:
    def distributeCandy(self, root):
        moves_required = [0]  # To keep track of moves required, using a list to be mutable

        def dfs(node):
            if not node:
                return 0

            left_moves = dfs(node.left)
            right_moves = dfs(node.right)

            # Calculate moves required for the current subtree rooted at 'node'
            moves_required[0] += abs(left_moves) + abs(right_moves)

            # Return the total number of candies in the subtree rooted at 'node'
            return node.data + left_moves + right_moves - 1

        dfs(root)

        return moves_required[0]
