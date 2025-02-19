class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        min_heap = []
        for node in arr:
            if node:
                heapq.heappush(min_heap, (node.data, id(node), node))
                
        # Dummy node to ease merging.
        dummy = Node(0)
        current = dummy
        
        # While there are nodes in the heap, extract the smallest node,
        # add it to our merged list, and push its next node into the heap.
        while min_heap:
            val, node_id, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.data, id(node.next), node.next))
        
        return dummy.next
