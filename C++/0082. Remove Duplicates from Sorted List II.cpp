class Solution {
public:
    ListNode* deleteDuplicates__(ListNode* head) {
        ListNode* dummpy = new ListNode(-101,head);
        ListNode* prev = dummpy;
        ListNode* curr = head;
        
        while (curr &&curr->next)
        {
            if(curr->val == curr->next->val)
            {
                while (curr &&curr->next && curr->val == curr->next->val){
                    curr = curr->next;
                }
                prev->next = curr->next;
            }              
            else    
            {                
                prev = curr;             
            }
          curr = curr->next;
        }
        return dummpy->next;
        
        
    }
    
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummpy = new ListNode(-101,head);
        ListNode* curr = dummpy;
        
        while (curr->next &&curr->next->next)
        {
            if(curr->next->val == curr->next->next->val)
            {
                int val_prev = curr->next->val;
                while (curr->next && curr->next->val == val_prev){
                    curr->next = curr->next->next;
                }             
            } 
            else            
                curr = curr->next;
        }
        return dummpy->next;
        
        
    }
};