/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int getNodeLength(ListNode * head){    
        int count = 0;
        while(head){
            ++count;
            head = head->next; 
        }
        return count;
    }
    
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
            int length1 = getNodeLength(headA);
            int length2 = getNodeLength(headB);
            ListNode * ptr1 = length1 >= length2 ? headA:headB;
            ListNode * ptr2 = length1 < length2 ? headA:headB;
            int diff = abs(length1 - length2);
            //move let prt1 len = ptr2 = len    
            while (diff--){
                ptr1 = ptr1->next;      
            }

            while(ptr1 && ptr2){
                if(ptr1 == ptr2){
                    return ptr1;
                }
                ptr1 = ptr1->next;
                ptr2 = ptr2->next;
            }    
            return nullptr;
    }
};