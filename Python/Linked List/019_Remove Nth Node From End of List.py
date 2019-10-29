'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1
        p = head
        while p.next:           
            length += 1
            p = p.next        
        
        n = length - n
        p = head
        if n == 0:
            return head.next
            
        index = 1
        while p.next:
            if index == n:
                p.next = p.next.next
                return head
            index += 1
            p = p.next
        return head        

    def removeNthFromEnd_simply(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head 
        while first:
            length += 1
            p = p.next

        length -= n

        first = dummy
        while length:
            length -= 1
            first = first.next
            
        first.next = first.next.next
        return dummy.next  


        
l1 = ListNode(1)
l1.next =  ListNode(2)
l1.next.next =  ListNode(3)  
l1.next.next.next =  ListNode(4)  
l1.next.next.next.next =  ListNode(5)        
        
        
sol = Solution()
sol.removeNthFromEnd(l1,2)        
        
l2 = ListNode(1)   
sol.removeNthFromEnd(l2,1)        
        
        
        
        
        
        
        

