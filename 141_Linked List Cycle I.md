# Linked List Cycle I


## 原題目:
```
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


Example 1:

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
    
Example 3:

    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

```

## 思路
利用set判斷node是否出現,如果出現表示有cycle




## Code



``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        exist = set()
        
        
        while head:
            if head in exist:
                return True
            exist.add(head)
            head = head.next
        return False
```  



## 思路

假設起點距離loop為X ,loop 一圈長度Y

<img src="141_1.png">


1.判斷是否為loop </br>
假設有2個指針fast,slow ,fast 指針一次走2步,slow 指針一次一步
若如果兩個指針會在同一地方相遇,表示為loop</br>
若fast 指針走完,表示沒loop</br>

## Code



``` python
class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
        return False
```  












