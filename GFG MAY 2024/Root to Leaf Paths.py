class Solution:
    def help(self, root, temp, ans):
        if root==None:
            return
        if root.left==None and root.right==None:
            temp.append(root.data)
            ans.append(temp[:])
            temp.pop()
            return
        temp.append(root.data)
        self.help(root.left, temp, ans)
        self.help(root.right, temp, ans)
        temp.pop()


    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        ans=[]
        temp=[]
        self.help(root, temp, ans)
        return ans
