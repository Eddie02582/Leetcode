# Merge Two Sorted Lists

## 原題目:
```
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
```

## 思路
迴圈比較大小,離開條件為其中1個List 為None,後面直接加上非None的List

## Code

#### Python

```python
class Solution:
     def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head        
        while l1 and l2 :            
            if  l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next            
            current = current.next                              

        urrent.next= l1 or l2
        
        return head.next
        
```

#### c++

<a href = "https://leetcode.com/submissions/detail/567095477/">100%</a>
```c++
class Solution {
public:   
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
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
```

```c++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
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
```



```






