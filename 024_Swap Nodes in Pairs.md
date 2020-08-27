# Remove Duplicates from Sorted Array

## 原題目:
```
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
```

## 思路
要如何對調,1->2->3->4->5,假設3和4對調,換成1->2->4->3->5 那麼需要將3->5,2->4,4->3,所以需要記錄的是pair node,pair node前一項,pair node後一項,即可<br>
因為1->2前面沒有東西,補個結點方便處理,也方便最後回傳結果(這方法在listnode的題目很常見)



<a href = "https://leetcode.com/submissions/detail/386908005/">Leet code SOL(99%)</a>

## Code

#### Python

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = ListNode(0,head)
        current = head
        prev = node
        while current and current.next:
            #record node
            node1 = current
            node2 = current.next
            _next = node2.next
            
            #swap
            node1.next = _next            
            node2.next = node1            
            prev.next  = node2 
            
            #update prev node and current node
            prev = node1  
            current = prev.next   
        return node.next  
```





