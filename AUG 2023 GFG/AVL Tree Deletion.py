#def deleteNode(root, key):
    # code here
    # return root of edited tree
def height(node):
    if node is None:
        return 0
    return node.height

def update_height(node):
    if node is None:
        return 0
    node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def rotate_left(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    update_height(z)
    update_height(y)

    return y

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x

def rebalance(node):
    update_height(node)
    balance = balance_factor(node)

    # Left heavy
    if balance > 1:
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    # Right heavy
    if balance < -1:
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        min_node = find_min(root.right)
        root.data = min_node.data
        root.right = deleteNode(root.right, min_node.data)

    return rebalance(root)

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def delete_values(root, values):
    for val in values:
        root = deleteNode(root, val)
    return root
