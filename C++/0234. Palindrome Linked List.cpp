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
    bool isPalindrome(ListNode* head) {
        vector<int> values ;
        ListNode *fast = head;
        ListNode *slow = head; 
        
        while (fast && fast->next){            
            values.push_back(slow->val);
            fast = fast->next->next;
            slow = slow->next;
        }
        
        if(fast)           
            slow = slow->next;            
      
        
        while (slow != NULL){     
            if(slow->val != values.back())
               return false;
            values.pop_back();
            slow = slow->next;
        }
        return true;
    }
};