class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vow = []
        con = []
        
        current_node = head
        while current_node:
            if current_node.data in vowels:
                vow.append(current_node.data)
            else:
                con.append(current_node.data)
            current_node = current_node.next
        final = vow+con
        head = None
        for i in range(len(final) - 1, -1, -1):
            temp = Node(final[i])
            temp.next = head
            head = temp
        return head
