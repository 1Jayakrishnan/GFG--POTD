class Solution:
    def findTarget(self, root, target): 
        if not root:
            return False
        
        # Two stacks for the two iterators:
        leftStack, rightStack = [], []
        
        # Helper: push all left children from node onto leftStack.
        def pushAllLeft(node):
            while node:
                leftStack.append(node)
                node = node.left
        
        # Helper: push all right children from node onto rightStack.
        def pushAllRight(node):
            while node:
                rightStack.append(node)
                node = node.right
        
        # Initialize the stacks.
        pushAllLeft(root)
        pushAllRight(root)
        
        # Helper: Get next smallest value from leftStack (in-order).
        def getNextSmallest():
            if not leftStack:
                return None
            node = leftStack.pop()
            val = node.data
            pushAllLeft(node.right)
            return val
        
        # Helper: Get next largest value from rightStack (reverse in-order).
        def getNextLargest():
            if not rightStack:
                return None
            node = rightStack.pop()
            val = node.data
            pushAllRight(node.left)
            return val
        
        # Initialize two pointers.
        leftVal = getNextSmallest()
        rightVal = getNextLargest()
        
        # Two-pointer approach: move the pointer with the smaller sum.
        while leftVal is not None and rightVal is not None and leftVal < rightVal:
            currentSum = leftVal + rightVal
            if currentSum == target:
                return True
            elif currentSum < target:
                leftVal = getNextSmallest()
            else:
                rightVal = getNextLargest()
                
        return False
