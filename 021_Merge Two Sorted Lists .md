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
                              
        if l1:
            current.next= l1
        else:
            current.next= l2
        
        return head.next
        
```







