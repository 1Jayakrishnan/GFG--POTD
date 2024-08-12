class Solution {
    // Function to rotate a linked list.
    public Node rotate(Node head, int k) {
        // add code here
        if(head == null && head.next == null){
            return head;
        }
        int size =0;
        Node temp = head;
        Node last = null;
        while(temp != null){
            size++;
            last = temp;
            temp = temp.next;
        }
        
        Node curr = head;
        Node next = head.next;
        while(k > 0){
            curr.next = null;
            last.next = curr;
            last = last.next;
            curr = next;
            next = curr.next;
            k--;
        }
        return curr;
    }
}
