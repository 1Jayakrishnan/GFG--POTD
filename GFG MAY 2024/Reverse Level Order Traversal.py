from collections import deque

def reverseLevelOrder(root):
    if not root:
        return []

    # Initialize a queue and a stack
    queue = deque()
    stack = []

    # Enqueue the root node
    queue.append(root)

    # Perform reverse level order traversal
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        
        # Push the node onto the stack
        stack.append(node.data)

        # Enqueue the children of the dequeued node (if any)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    # Reverse the stack to get the reverse level order traversal
    return stack[::-1]
