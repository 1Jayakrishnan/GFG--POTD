class Solution:
    def cloneLinkedList(self, head):
        new=[]
        rand=[]
        dct={}
        
        dummy=Node(None)
        ncur=dummy
        
        idx=0
        cur=head
        while cur:
            ncur.next=Node(None)
            ncur=ncur.next
            ncur.data=cur.data
            new.append(ncur)
            dct[cur]=idx
            rand.append(cur.random)
            cur=cur.next
            idx+=1
        
        cur=dummy.next
        for nd in rand:
            if nd:
                cur.random=new[dct[nd]]
            cur=cur.next
        
        return dummy.next
