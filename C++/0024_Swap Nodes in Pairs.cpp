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
        if (!head)
			return head;
		
		ListNode* dummy = new ListNode(0,head);
		ListNode* prevNode = dummy;
		ListNode* curr = head;
		while(curr && curr->next ){
			ListNode* next = curr->next;			
			//1->3
			curr->next = curr->next->next;
			//0->2
			prevNode->next = next;
			//2->1
			next->next = curr;
			
			//update
			prevNode = curr;
			curr = curr->next;
			
		}
		
		return dummy->next;
    }
};