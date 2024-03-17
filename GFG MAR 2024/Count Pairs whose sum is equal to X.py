class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        count = 0
        set1 = set()
        
        # Add elements of the first linked list to the hash set
        current = head1
        while current:
            set1.add(current.data)
            current = current.next
        
        # Iterate through the elements of the second linked list
        current = head2
        while current:
            complement = x - current.data
            if complement in set1:
                count += 1
            current = current.next
        
        return count
