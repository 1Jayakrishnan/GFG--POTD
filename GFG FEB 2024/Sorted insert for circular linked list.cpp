class Solution {
public:
    Node* sortedInsert(Node* head, int data) {
        // Create a new node with the given data
        Node* newNode = new Node(data);

        // If the list is empty, make the new node the head and point it to itself
        if (!head) {
            newNode->next = newNode;
            return newNode;
        }

        // If the new node should be inserted before the head
        if (data < head->data) {
            // Find the last node in the list
            Node* last = head;
            while (last->next != head) {
                last = last->next;
            }

            // Update pointers to insert the new node at the beginning
            last->next = newNode;
            newNode->next = head;
            return newNode;
        }

        // Find the node after which the new node should be inserted
        Node* curr = head;
        while (curr->next != head && curr->next->data < data) {
            curr = curr->next;
        }

        // Update pointers to insert the new node at the correct position
        newNode->next = curr->next;
        curr->next = newNode;

        return head;
    }
};
