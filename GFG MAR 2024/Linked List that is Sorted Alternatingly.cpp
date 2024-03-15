class Solution
{
    public:
    // your task is to complete this function
    void sort(Node **head)
    {
        // Code here
        Node *temp = *head;
        vector<int> v;
        while(temp!=NULL){
            v.push_back(temp->data);
            temp = temp->next;
        }
        
        ::sort(v.begin(),v.end());
        
        Node*p = *head;
        int i = 0;
        while(p!=NULL){
            p->data = v[i];
            p = p->next;
            i++;
        }
        
    }
};
