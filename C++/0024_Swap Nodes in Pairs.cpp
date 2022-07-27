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
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* curr = head;  
        ListNode* prev = dummy;         
        while (curr && curr->next){  
            
            ListNode* node1 = curr;
            ListNode* node2 = curr->next;
            // 0->1->2->3   0->2->1->3
            node1->next = node2->next; //1->3
            prev->next = node2;   //0->2
            node2->next = node1;  // 2->1  
            //update
            prev = node1;              
            curr = node1->next; 
          
        }        
        return dummy->next;
    }
};