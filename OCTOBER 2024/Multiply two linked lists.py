class Solution:
    MOD = 10**9 + 7
    
    # Helper function to convert linked list to an integer
    def listToNumber(self, head):
        num = 0
        while head:
            num = (num * 10 + head.data) % self.MOD
            head = head.next
        return num

    # Function to multiply two linked lists
    def multiply_two_lists(self, l1, l2):
        # Convert both linked lists to numbers
        num1 = self.listToNumber(l1)
        num2 = self.listToNumber(l2)
        
        # Multiply the two numbers and take modulo
        return (num1 * num2) % self.MOD
