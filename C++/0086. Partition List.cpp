class Solution {
public:
    ListNode *partition(ListNode *head, int x) {
        
        ListNode * small = new ListNode(0);
        ListNode * high = new ListNode(0);
        ListNode * smallhead = small;
        ListNode * highhead = high;
        while(head){
            if(head->val<x){
                //small list
                smallhead->next=head;
                smallhead = smallhead->next;
            }
            else{
                  //high list
                highhead->next=head;
                highhead = highhead->next;
            }
            head=head->next;
        }

        //merge the two lists
        highhead->next = NULL;
        smallhead->next = high->next;

        return small->next;
    }
};