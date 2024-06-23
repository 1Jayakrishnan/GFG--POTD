class Solution:
    def bracketNumbers(self, str):
        # code here
        stack=[]
        list1=[]
        count=1
        for i in str:
            if i=='(':
                stack.append(count)
                list1.append(count)
                count+=1
            elif i==')':
                popout=stack.pop()
                list1.append(popout)
        return list1
