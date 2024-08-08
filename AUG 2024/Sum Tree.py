class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def is_sum_tree(self, node):
        def check_sum_tree(node):
            if node is None:
                return 0, True
            
            if node.left is None and node.right is None:
                return node.data, True
            
            left_sum, left_is_sum_tree = check_sum_tree(node.left)
            right_sum, right_is_sum_tree = check_sum_tree(node.right)
            
            total_sum = left_sum + right_sum
            
            if node.data == total_sum and left_is_sum_tree and right_is_sum_tree:
                return total_sum + node.data, True
            else:
                return total_sum + node.data, False
        
        _, is_sum_tree_result = check_sum_tree(node)
        return is_sum_tree_result
