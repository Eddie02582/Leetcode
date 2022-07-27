# 82. Remove Duplicates from Sorted List II

## 原題目:
```
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:

    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]
    
Example 2:
    Input: head = [1,1,1,2,3]
    Output: [2,3]
```

## 思路


#### c++



``` c++
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummpy = new ListNode(-101,head);
        ListNode* prev = dummpy;
        ListNode* curr = head;
        
        while (curr &&curr->next)
        {
            if(curr->val == curr->next->val)
            {
                while (curr &&curr->next && curr->val == curr->next->val){
                    curr = curr->next;
                }
                prev->next = curr->next;
            }              
            else    
            {                
                prev = curr;             
            }
          curr = curr->next;
        }
        return dummpy->next;
        
        
    }  
};
``` 


## 思路2

#### c++

``` c++
class Solution {
public:    
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummpy = new ListNode(-101,head);
        ListNode* curr = dummpy;
        
        while (curr->next &&curr->next->next)
        {
            if(curr->next->val == curr->next->next->val)
            {
                int val_prev = curr->next->val;
                while (curr->next && curr->next->val == val_prev){
                    curr->next = curr->next->next;
                }             
            } 
            else            
                curr = curr->next;
        }
        return dummpy->next;
        
        
    }
};
``` 


