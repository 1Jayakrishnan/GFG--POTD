class Solution:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        return self._reverse(head, k)
    
    def _reverse(self, head, k):
        prev, node = None, head
        for _ in range(k):
            if node is None:
                return prev
            prev, node.next, node = node, prev, node.next
        if node:
            head.next = self._reverse(node, k)
        return prev
