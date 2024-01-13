class Solution {
    static Node insertionSort(Node head) {
        if (head == null || head.next == null) {
            return head;
        }

        Node dummy = new Node(0);
        dummy.next = head;
        Node current = head;

        while (current != null && current.next != null) {
            if (current.data > current.next.data) {
                Node prev = dummy;
                Node target = dummy.next;

                while (target.data < current.next.data) {
                    prev = target;
                    target = target.next;
                }

                Node temp = current.next;
                current.next = temp.next;
                temp.next = target;
                prev.next = temp;
            } else {
                current = current.next;
            }
        }

        return dummy.next;
    }

}
