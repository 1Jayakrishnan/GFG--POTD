class Solution:
    def dupSub(self, root):
        # code here
        def check(node,dic) :
            
            if not node :
                return ""
                
            s = check(node.left,dic) + str(node.data) + check(node.right,dic)
            
            dic[s]=dic.get(s,0) + 1
            
            return s
        
        dic={}
        v=check(root,dic)
        
        for x in dic :
            if len(x) > 1 and dic[x] > 1 :
                return 1
        return 0
        
