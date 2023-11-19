#include <iostream>
class Solution {
public:
    Node* findIntersection(Node* head1, Node* head2) {
        Node* dummy = new Node(0); // Dummy node to simplify code
        Node* current = dummy;

        while (head1 != nullptr && head2 != nullptr) {
            if (head1->data == head2->data) {
                current->next = new Node(head1->data);
                current = current->next;
                head1 = head1->next;
                head2 = head2->next;
            } else if (head1->data < head2->data) {
                head1 = head1->next;
            } else {
                head2 = head2->next;
            }
        }

        return dummy->next; // Return the next of the dummy node, which is the start of the result linked list
    }
};
