from collections import defaultdict, deque

class Solution:
    def minTime(self, root, target):
        if not root:
            return 0
        
        # A helper function to map each node to its parent.
        def map_parents(node, parent, parent_map):
            if node:
                parent_map[node] = parent
                map_parents(node.left, node, parent_map)
                map_parents(node.right, node, parent_map)
        
        # A helper function to find the target node and its parent.
        def find_target(node, target):
            if node is None:
                return None
            if node.data == target:
                return node
            left_search = find_target(node.left, target)
            if left_search:
                return left_search
            return find_target(node.right, target)
        
        # Step 1: Map all nodes to their parents
        parent_map = defaultdict(lambda: None)
        map_parents(root, None, parent_map)
        
        # Step 2: Find the target node
        target_node = find_target(root, target)
        
        # Step 3: Perform BFS to simulate the burning process
        queue = deque([(target_node, 0)])  # (node, time)
        visited = set()
        visited.add(target_node)
        max_time = 0
        
        while queue:
            current_node, current_time = queue.popleft()
            max_time = max(max_time, current_time)
            
            # Visit left child
            if current_node.left and current_node.left not in visited:
                visited.add(current_node.left)
                queue.append((current_node.left, current_time + 1))
            
            # Visit right child
            if current_node.right and current_node.right not in visited:
                visited.add(current_node.right)
                queue.append((current_node.right, current_time + 1))
            
            # Visit parent
            parent = parent_map[current_node]
            if parent and parent not in visited:
                visited.add(parent)
                queue.append((parent, current_time + 1))
        
        return max_time
