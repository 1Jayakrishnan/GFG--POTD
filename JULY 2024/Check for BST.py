import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def check(node) :
            
            if not node :
                return [True,float('inf'),float('-inf')]
                
            if not node.left and not node.right :
                return [True,node.data,node.data]
                
            l=check(node.left)
            r=check(node.right)
            
            if l[0] and r[0] and l[2] < node.data < r[1] :
                return [True,min(l[1],node.data),max(r[2],node.data)]
            else :
                return [False,float('inf'),float('-inf')]
        
        return check(root)[0]
