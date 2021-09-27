# Remove Linked List Elements


## 原題目:
```
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
    
Example 2:
    Input: head = [], val = 1
    Output: []
    
Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []
 

Constraints:
    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50
```

## 思路
要刪除某個元素,就是將他的上個節點指向他得下個節點,一般來說是對下個節點判斷<br>



#### Python



``` python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val ==  val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next        
``` 

這邊是對當下節點判斷,注意這時候要儲存上個節點
```python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy 
        
        while head:            
            if head.val == val:
                prev.next = head.next                  
            else:
                prev = head
            head = head.next  
        return dummy.next
```



