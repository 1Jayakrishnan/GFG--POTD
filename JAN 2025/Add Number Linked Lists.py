class Solution:
    def addTwoLists(self, num1, num2):
        def rev(head):
            prv=None
            cur=head
            while cur:
                tmp=cur.next
                cur.next=prv
                prv=cur
                cur=tmp
            return prv
        num1=rev(num1)
        num2=rev(num2)
        carry=0
        ret=Node(0)
        cur=ret
        while num1 or num2 or carry:
            ve=(num1.data if num1 else 0)+(num2.data if num2 else 0)+carry
            cur.data=ve%10
            carry=1 if ve>=10 else 0
            num1=num1.next if num1 else None
            num2=num2.next if num2 else None
            cur.next=Node(0)
            cur=cur.next
        ret=rev(ret)
        while ret.data==0:
            ret=ret.next
        return ret
