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
        while(l1 && l2)
        {
            if(l1->val <= l2->val)            {
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
    ListNode* mergeTwoLists_2(ListNode* list1, ListNode* list2) {
        ListNode *head = new ListNode(0);
        ListNode *curr = head;
        
        while(list1 && list2){
            int val1 = list1->val;
            int val2 = list2->val;
            if(val1 <val2){
                curr->next = list1;
                list1 = list1->next;
            }
            else{
                curr->next = list2;
                list2 = list2->next;           
            }            
            curr = curr->next;            
        }
        if(list1)
            curr->next = list1;
        if(list2)
             curr->next = list2;         
        return head->next;
    }
};

