# Python code here
def compute(head):
    node = head
    nodes = []
    while node:
        nodes.append(node)
        node = node.next

    left, right = 0, len(nodes) -1
    lp, rp = 0, len(nodes[right].data)-1
    while left <= right:
        while lp < len(nodes[left].data) and rp >= 0:
            if nodes[left].data[lp] != nodes[right].data[rp]:
                return False
            lp += 1
            rp -= 1
        if lp >= len(nodes[left].data):
            left += 1
            lp = 0
        if rp < 0:
            right -= 1
            if right >= 0:
                rp = len(nodes[right].data)-1
    return True
