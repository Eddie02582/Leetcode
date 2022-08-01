# Partition List


## 原題目:
```
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
```

## 思路1


## Code

#### c++
把原本linklist分成比x大和小最後在合併
``` c++
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
```  
一樣的做法,只是順便將原本linklist改成比x大的,最後合併
``` c++
class Solution {
public:
    ListNode *partition(ListNode *head, int x) {
        if (!head) return head;
        ListNode *dummy= new ListNode(x,head);
        ListNode *newDummy= new ListNode(x);  
        ListNode *cur = dummy;
        ListNode *p= newDummy; 
        
        while (cur->next) {
            if(cur->next->val < x){    
                p->next = cur->next;
                p = p->next;
                cur->next = cur->next->next;               
            } else {
                cur = cur->next;
            }
        }
        p->next = dummy->next;
        return newDummy->next;
    }
};
```








