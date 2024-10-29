def quickSort(head):
    if not head or not head.next:
        return head  
    
    def partition(start, end):
        pivot, prev = start, None
        curr = start
        tail = pivot

        while curr != end:
            if curr.data < pivot.data:
                if prev:
                    prev.next = curr.next
                curr.next = start
                start = curr
                curr = prev.next if prev else tail.next
            else:
                prev = curr
                curr = curr.next
        return pivot, start, tail

    def quickSortRecur(start, end):
        if start == end or not start:
            return start
        pivot, left_head, pivot_tail = partition(start, end)
        left_head = quickSortRecur(left_head, pivot)
        pivot_tail.next = quickSortRecur(pivot.next, end)
        return left_head

    return quickSortRecur(head, None)
