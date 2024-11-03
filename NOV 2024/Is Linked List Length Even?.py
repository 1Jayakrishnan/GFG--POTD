def isLengthEven(self, head):
        # Code here
        l = 0
        while head != None:
            l += 1
            head = head.next
            
        if l%2 == 0:
            return 1
        else:
            return 0
            
