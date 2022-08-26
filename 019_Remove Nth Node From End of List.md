# Remove Nth Node From End of List


## 原題目:
```
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
    Given n will always be valid.
```

## 思路1
首先取得Linked List 的長度,並換算得出是第幾個要刪除,則其前一個節點並需讓next指向next.next<br>
注意這種做法,小心當移除位置剛好為第一項會有問題,需回傳head.next


## Code

#### Python

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        length  = 0
        while temp:
            length += 1
            temp = temp.next  
        
        remove_index ,index = length - n ,0       
        current = head
        
        if remove_index == 0:
            return head.next
            
        while current:
            index += 1
            if index == remove_index:
                current.next = current.next.next
            current = current.next
                
        return head 
```



## 思路2
改善上面的做法,再其前面新增一個假節點,就不需要特別處理當要拿掉第一個點時


## Code

#### c++
```python
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
 ```


## 思路3

## Code

#### c++

```c++
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
        ListNode* ptr1 = new ListNode(2, head);  
        ListNode* ptr2 = new ListNode(2, head);  
        ListNode* dummy = ptr2; 
        int step = 0;         
        while (step < (n + 1) && ptr1){
            ++step;
            ptr1 = ptr1->next;
        }        
   
        while (ptr1 &&　ptr2){          
            ptr2 = ptr2->next;            
            ptr1 = ptr1->next;
        }
     
        ptr2->next = ptr2->next->next;      
        
        return dummy->next;
    }
};
```



