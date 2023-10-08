class Solution {
public:
    Node* sortedInsert(Node* head, int data) {
        // Create a new node with the given data
        Node* new_node = new Node(data);
        
        // If the linked list is empty or the data is smaller than the head node's data,
        // insert the new node at the beginning of the list.
        if (!head || data <= head->data) {
            new_node->next = head;
            return new_node;
        }
        
        // Traverse the linked list to find the correct position to insert the new node.
        Node* current = head;
        while (current->next && current->next->data < data) {
            current = current->next;
        }
        
        // Insert the new node between the current node and the next node.
        new_node->next = current->next;
        current->next = new_node;
        
        return head;
    }
};
