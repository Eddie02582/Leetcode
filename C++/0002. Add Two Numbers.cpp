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
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int carry = 0;
        while (l1  || l2)
        {
            int n = carry;
            if (l1){        
                n += l1->val;
                l1 = l1->next;
            }
            if (l2)  {       
                n += l2->val;         
                l2 = l2->next; 
            }
            carry = 0;
            if (n > 9){
                carry = 1;
                n -= 10;
            }         
            curr->next = new ListNode(n);   
            curr = curr->next;
        }
        if (carry)
            curr->next = new ListNode(1);
        
        return dummy->next;
    }
};