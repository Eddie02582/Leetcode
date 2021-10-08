// Your First C++ Program

#include <iostream>
#include <vector>

using namespace std;


struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {       
        ListNode *head= new ListNode();       
        ListNode *dummy = head;
        
        while(l1 !=NULL && l2 !=NULL)
        {
            if(l1->val <= l2->val)
            {
                dummy->next = new ListNode(l1->val);
                l1 = l1->next;
            }
            else{
                 dummy->next = new ListNode(l2->val);
                 l2 = l2->next;
            }  
            dummy = dummy->next;   
        }   
        dummy->next = l1 !=NULL? l1:l2;             
        return head->next;

    }
    //下面這個比較快
    ListNode* mergeTwoLists_2(ListNode* l1, ListNode* l2) {
        ListNode head (0);       
        ListNode *dummy = &head;        
        while(l1 !=NULL && l2 !=NULL)
        {
            if(l1->val <= l2->val)
            {
                dummy->next = new ListNode(l1->val);
                l1 = l1->next;
            }
            else{
                dummy->next = new ListNode(l2->val);
                l2 = l2->next;
            }  
            dummy = dummy->next;    
        } 
        dummy->next = l1 !=NULL? l1:l2;   
        return head.next;
    }


};

