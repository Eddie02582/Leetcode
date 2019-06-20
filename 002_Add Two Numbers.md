# Two Sum


## 原題目:
```
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
'''
```

## 思路

設立一個表示進位的變量carried，建立一個新鍊錶，把輸入的兩個鍊錶從頭往後同時處理，每兩個相加，將結果加上carried後的值作為一個新節點到新鍊錶後面。

<img src="https://github.com/Eddie02582/Leetcode/blob/master/picture/2.addTwoNumbers.gif" alt="Smiley face">

(图片来自：<a href="https://github.com/MisterBooo/LeetCodeAnimation">https://github.com/MisterBooo/LeetCodeAnimation</a>)


## Code

#### Python

``` python
class Solution:   
    def addTwoNumbers(self, l1, l2):
    
        head=ListNode(0)        
        current = head
        carried = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            n = (carried + x + y) % 10
            carried = (carried + x + y) // 10;
            current.next = ListNode(n)
            current = current.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        if carried:
            current.next = ListNode(carried)        
        return head.next
```  

