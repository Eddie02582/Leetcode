'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution:   
    def addTwoNumbers(self, l1, l2):
    
        head=ListNode(0)        
        current = head
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            n = (carry + x + y) % 10
            carry = (carry + x + y) // 10;
            current.next = ListNode(n)
            current = current.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            current.next = ListNode(carry)
        
        return head.next
  
l1 = ListNode(2)
l1.next =  ListNode(4)
l1.next.next =  ListNode(3)

l2 = ListNode(5)
l2.next =  ListNode(6)
l2.next.next =  ListNode(4)
  
sol= Solution()

sol.addTwoNumbers(l1,l2)