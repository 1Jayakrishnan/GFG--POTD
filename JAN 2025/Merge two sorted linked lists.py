class Solution:
    def sortedMerge(self, head1, head2):
        temp = Node(0)
        curr = temp
        m, n = head1, head2
        
        while m and n:
            if m.data < n.data:
                curr.next = m
                curr = m
                m = m.next
            elif m.data > n.data:
                curr.next = n
                curr = n
                n = n.next
            else:
                curr.next = m
                curr = m
                m = m.next
                curr.next = n
                curr = n
                n = n.next
        
        while m:
            curr.next = m
            curr = m
            m = m.next
        
        while n:
            curr.next = n
            curr = n
            n = n.next
        
        return temp.next
