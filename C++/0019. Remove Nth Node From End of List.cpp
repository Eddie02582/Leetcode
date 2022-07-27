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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);        
        ListNode * curr = head;
        int size = 1;
        while (curr->next){
            ++size;
            curr = curr->next;
        }
        
        int removeIndex = size - n;
        curr = dummy;        
        while (removeIndex--)
        {
            curr = curr->next;
        }
        curr->next = curr->next->next;
        return dummy->next;
    }
};