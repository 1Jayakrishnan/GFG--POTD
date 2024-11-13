class Intersect {
    // Function to find intersection point in Y shaped Linked Lists.
    int intersectPoint(Node head1, Node head2) {
        if (head1 == null || head2 == null) {
            return -1; // If either list is empty, no intersection.
        }
        Node current1 = head1;
        Node current2 = head2;
        // Traverse both lists
        while (current1 != current2) {
            // Move to the next node or switch to the other list if at the end
            current1 = (current1 == null) ? head2 : current1.next;
            current2 = (current2 == null) ? head1 : current2.next;
        }
        // If they meet at null, it means there's no intersection
        return (current1 != null) ? current1.data : -1;
    }
}
