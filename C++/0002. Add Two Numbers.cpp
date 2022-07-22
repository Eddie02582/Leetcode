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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head= new ListNode(0);       
        ListNode *dummy = head;   
        int carry = 0;    
        while(l1 != NULL || l2 != NULL){
            int n1 = 0,
            int n2 = 0;            
            if (l1 != NULL)
            {
                n1 = l1->val;
                l1 = l1->next; 
            }
            if (l2 != NULL)
            {
                n2 = l2->val;
                l2 = l2->next; 
            }
            int res = n1 + n2 + carry;
            carry = 0;
            if (res > 9)
            {
                carry = 1;
                res -= 10;
            }   
            
            dummy->next = new ListNode(res);     
            dummy = dummy->next;          
        }
        if(carry >0)
            dummy->next = new ListNode(carry);  

        return head->next;
    }
};