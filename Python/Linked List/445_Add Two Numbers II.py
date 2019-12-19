# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1,n2 = 0,0
        while l1:        
            n1 = 10 * n1 + l1.val        
            l1 = l1.next 
        while l2:        
            n2 = 10 * n2 + l2.val        
            l2 = l2.next
        n = n1 + n2
        
        head = ListNode(0)       
        current = head
        for s in str(n):
            head.next = ListNode(int(s))
            head = head.next   
        return current.next        
        
        
        
        
    def addTwoNumbers__(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_1 = []
        stack_2 = []
        cur1, cur2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        while cur1:
            stack_1.append(cur1)
            cur1 = cur1.next
        while cur2:
            stack_2.append(cur2)
            cur2 = cur2.next
        while carry or stack_1 or stack_2:
            x1 = stack_1.pop().val if stack_1 else 0
            x2 = stack_2.pop().val if stack_2 else 0
            tmp = ListNode((x1 + x2 + carry) % 10)
            tmp.next = dummy.next
            dummy.next = tmp
            carry = (x1 + x2 + carry) // 10
        return dummy.next        
        