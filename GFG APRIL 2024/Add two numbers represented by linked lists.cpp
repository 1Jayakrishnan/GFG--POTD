class Solution
{
    public:
    void reverseNode(struct Node*& head) {
        if (head == NULL || head->next == NULL)
            return;
        
        Node* prev = NULL;
        Node* current = head;
        Node* next;
    
        while (current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
    
        head = prev;
    }
    
    void insertAtBeginning(struct Node*& head, int data){
        Node* temp = new Node(data);
        temp -> next = head;
        head = temp;
    }
    
    struct Node* addTwoLists(struct Node* num1, struct Node* num2)
    {
        //Removes Unneccessary zeros
        while(num1->data == 0 && num1->next != NULL)
            num1 = num1->next;
        while(num2->data == 0 && num2->next != NULL)
            num2 = num2->next;
        
        reverseNode(num1);
        reverseNode(num2);
            
        Node* sum = NULL;
        
        //Carry
        int c = 0;
        
        while (num1 || num2 || c){
            //temporary sum
            int s = c;
            if (num1){
                s += num1->data;
                num1 = num1->next;
            }
            if (num2){
                s += num2->data;
                num2 = num2->next;
            }
            insertAtBeginning(sum, s%10);
            c = s/10;
        }
           
        return sum;
    }
};
