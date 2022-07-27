/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if ( k == 0 || head == NULL)
            return head;        
       
        //find ListNode Length
        ListNode* p = head;
        int linkLength = 1; 
        
        while (p ->next != NULL){
            p = p->next;
            ++linkLength;
        }             
        //not need rotate
        if(k % linkLength == 0)
            return head;
        
        //find rotate prev item
        int cutLocation = linkLength -k % linkLength - 1;    
        ListNode* q = head;        
        while (cutLocation--){           
            q = q->next;  
        }     
        
        //new head equql cut item next        
        ListNode *newHead = q->next;
        q->next = NULL;
        
        // new head last item need to pointer to head    
        p->next = head;        
        return newHead; 
    }
};