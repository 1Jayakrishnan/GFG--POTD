def convert(head):
    a = []
    
    curr = head
    n=0
    while curr!=None:
        a.append(curr.data)
        curr = curr.next
        n += 1
        
    def buildTree(i):
        if i>=n:
            return
        newNode = Tree(a[i])
        left = buildTree(2*i+1)
        right = buildTree(2*i+2)
        newNode.left = left
        newNode.right = right
        return newNode
        
    root = buildTree(0)
    return root
