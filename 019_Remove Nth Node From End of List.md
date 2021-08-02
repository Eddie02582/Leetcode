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
改善上面的做法,再其前面新增一個假節點,這邊採用length--的做法


## Code

#### Python
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        runner = head       
        for _ in range(n):
            runner = runner.next

        dummy = walker = ListNode(next=head)

        while runner:
            walker = walker.next
            runner = runner.next
           
        walker.next = walker.next.next
        return dummy.next
 ```







